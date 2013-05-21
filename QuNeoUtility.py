from ConfigurableButtonElement import ConfigurableButtonElement
from _Framework.InputControlElement import *
from MIDI_Map import *

class QuNeoUtility(object):
  """ Provides some functionality shared across ALL classes """

  def button(self, channel, note, color = GREEN_HI):
    return ConfigurableButtonElement(True, MIDI_NOTE_TYPE, channel, note, color)
