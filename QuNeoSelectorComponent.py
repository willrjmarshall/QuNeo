from _Framework.ModeSelectorComponent import ModeSelectorComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.InputControlElement import *
from MIDI_Map import *

class QuNeoSelectorComponent(ModeSelectorComponent):
  """ Class that reassigns the QuNeo Matrix between session control and step sequencer modes """

  def __init__(self, matrix_notes, shift_button): 
    ModeSelectorComponent.__init__(self)
    self.shift_button = None
    self.setup_shift(shift_button)
    self.setup_matrix(matrix_notes)
    self.setup_session(self._matrix)

  def setup_matrix(self, matrix_notes):
    self._matrix = ButtonMatrixElement()
    for row in matrix_notes:
      button_row = []
      for note in row:
        button_row.append(ButtonElement(True, MIDI_NOTE_TYPE, PAD_CHANNEL, note))
      self._matrix.add_row(tuple(button_row))

  def setup_session(self, matrix):
    self._session = SessionComponent(matrix.width(), matrix.height()) 

  def setup_shift(self, shift_button):
    shift_button = ButtonElement(True, MIDI_NOTE_TYPE, PAD_CHANNEL, shift_button) 
    if (self.shift_button != shift_button):
      if (self.shift_button != None):
          self.shift_button.remove_value_listener(self._shift_value)
      self.shift_button = shift_button
      if (self.shift_button != None):
          self.shift_button.add_value_listener(self._shift_value)

  def _shift_value(self, value):
    if value > 0:
      self.shift_on()
    else:
      self.shift_off()

  def shift_on(self):
    self.shift_button.turn_on()

  def shift_off(self):
    self.shift_button.turn_off()

  def setup_buttons(mode_buttons):
    self.set_mode_buttons([self.button(note) for note in mode_buttons])
    #self._directional_buttons = [self.button(note) for note in directional_buttons]
    

  def number_of_modes(self):
    return 2

  def update(self):
    pass
