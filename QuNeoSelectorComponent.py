from _Framework.ModeSelectorComponent import ModeSelectorComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.InputControlElement import *
from MIDI_Map import *
from SubSelectorComponent import SubSelectorComponent
from QuNeoSessionComponent import QuNeoSessionComponent
from QuNeoSequencer import QuNeoSequencer

class QuNeoSelectorComponent(ModeSelectorComponent):
  """ Class that reassigns the QuNeo Matrix between default mode and mode selector mode 
      Default mode just renders whatever the SubSelector has selected

      ALL THE INTERESTING BITS ARE IN THE SUBSELECTOR
  """

  def __init__(self, matrix_notes, shift_button): 
    ModeSelectorComponent.__init__(self)
    self.setup_matrix(matrix_notes)
    self.setup_session(self._matrix)
    self.setup_sequencer(self._matrix)
    self.setup_subselector()
    self.setup_toggle(shift_button)

  def setup_matrix(self, matrix_notes):
    self._matrix = ButtonMatrixElement()
    for row in matrix_notes:
      button_row = []
      for note in row:
        button_row.append(ButtonElement(True, MIDI_NOTE_TYPE, GRID_CHANNEL, note))
      self._matrix.add_row(tuple(button_row))

  def setup_sequencer(self, matrix):
    self._sequencer = QuNeoSequencer(matrix, self._session)

  def setup_session(self, matrix):
    self._session = QuNeoSessionComponent(matrix) 
    self._session.set_offsets(0,0)
    #self._session.set_select_buttons(self.button(PAD_CHANNEL, SCENE_DOWN), self.button(PAD_CHANNEL, SCENE_UP))

  def setup_subselector(self):
    self._sub_modes = SubSelectorComponent(self._matrix, self._session, self._sequencer, self)
    self._sub_modes.set_mode(0)

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
    self._sub_modes.update()

  def mode(self):
    return self._mode_index

