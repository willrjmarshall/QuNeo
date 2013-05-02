from _Framework.ModeSelectorComponent import ModeSelectorComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.InputControlElement import *
from MIDI_Map import *
from SubSelectorComponent import SubSelectorComponent
from QuNeoSessionComponent import QuNeoSessionComponent

class QuNeoSelectorComponent(ModeSelectorComponent):
  """ Class that reassigns the QuNeo Matrix between default mode and mode selector mode 
      Default mode just renders whatever the SubSelector has selected
  """

  def __init__(self, matrix_notes, shift_button): 
    self.shift_button = None
    self.setup_matrix(matrix_notes)
    self.setup_session(self._matrix, True)
    self.setup_subselector()

    ModeSelectorComponent.__init__(self)
    self.setup_toggle(shift_button)

  def setup_subselector(self):
    self._sub_modes = SubSelectorComponent(self._matrix, self._session)
    self._sub_modes.set_mode(0)

  def setup_matrix(self, matrix_notes):
    self._matrix = ButtonMatrixElement()
    for row in matrix_notes:
      button_row = []
      for note in row:
        button_row.append(ButtonElement(True, MIDI_NOTE_TYPE, GRID_CHANNEL, note))
      self._matrix.add_row(tuple(button_row))

  def setup_session(self, matrix, as_active):
    self._session = QuNeoSessionComponent(matrix) 

  def setup_toggle(self, shift_button):
    self.set_mode_toggle(ButtonElement(True, MIDI_NOTE_TYPE, PAD_CHANNEL, shift_button))

  def _toggle_value(self, value):
    if self._mode_toggle != None:
      if value > 0:
        self.set_mode(1)
        self._mode_toggle.turn_on()
      else:
        self.set_mode(0)
        self._mode_toggle.turn_off()
    
  def number_of_modes(self):
    return 2

  def update(self):
    if self.mode() == 0: 
      self._session.setup()
      self._sub_modes._setup_mode_buttons(as_active = False)
      self._session.update()
    else:
      self._session.setup(as_active = False)
      self._sub_modes._setup_mode_buttons()

  def mode(self):
    return self._mode_index
