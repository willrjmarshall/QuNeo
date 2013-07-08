from _Framework.MixerComponent import MixerComponent
from QuNeoUtility import QuNeoUtility
from MIDI_Map import *

class QuNeoMixer(MixerComponent, QuNeoUtility):
  def __init__(self):
    MixerComponent.__init__(self, 8)
    self.sends = []
    self.setup()

  def setup(self, as_active = True):
    if as_active:
      self.set_crossfader_control(self.encoder(PAD_CHANNEL, CROSSFADER))
      for track in range(8):
        strip = self.channel_strip(track) 
        if track < 4:
          strip.set_volume_control(self.encoder(SLIDER_CHANNEL, TRACK_VOL[track]))

      for index in range(2):
        self.sends.append(self.encoder(SLIDER_CHANNEL, SELECTED_SENDS[index]))
      self.selected_strip().set_send_controls(tuple(self.sends))
      self.selected_strip().set_pan_control(self.encoder(SLIDER_CHANNEL, SELECTED_PAN))
      self.selected_strip().set_volume_control(self.encoder(SLIDER_CHANNEL, SELECTED_VOL))

      self.set_select_buttons(
          self.button(PAD_CHANNEL, TRACK_RIGHT),
          self.button(PAD_CHANNEL, TRACK_LEFT))


    else:
      self.set_crossfader_control(None)
      for track in range(8):
        strip = self.channel_strip(track) 
        if track < 4:
          strip.set_volume_control(None)
      self.sends = []
      self.selected_strip().set_send_controls(tuple(self.sends))
      self.selected_strip().set_pan_control(None)
      self.selected_strip().set_volume_control(None)
      self.set_select_buttons(None, None)
      self.set_bank_buttons(None, None)
