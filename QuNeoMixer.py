from _Framework.MixerComponent import MixerComponent
from QuNeoUtility import QuNeoUtility
from MIDI_Map import *

class QuNeoMixer(MixerComponent, QuNeoUtility):
  def __init__(self):
    MixerComponent.__init__(self, 8)
    self.set_crossfader_control(self.encoder(PAD_CHANNEL, CROSSFADER))
    for track in range(8):
      strip = self.channel_strip(track) 
      if track < 4:
        strip.set_volume_control(self.encoder(SLIDER_CHANNEL, TRACK_VOL[track]))



