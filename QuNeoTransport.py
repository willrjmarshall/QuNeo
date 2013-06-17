from _Framework.TransportComponent import TransportComponent
from QuNeoUtility import QuNeoUtility
from MIDI_Map import *

class QuNeoTransport(TransportComponent, QuNeoUtility):

  def __init__(self):
    TransportComponent.__init__(self)
    self.set_play_button(self.button(PAD_CHANNEL, PLAY))
    self.set_record_button(self.button(PAD_CHANNEL, REC))
    self.set_stop_button(self.button(PAD_CHANNEL, STOP))
