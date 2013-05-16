from _Framework.ModeSelectorComponent import ModeSelectorComponent
from MIDI_Map import *

class SubSelectorComponent(ModeSelectorComponent):
  """ Subselector that switches between session and sequencer modes """

  def __init__(self, matrix, session, parent): 
    ModeSelectorComponent.__init__(self)
    self._matrix = matrix
    self._session = session
    self._parent = parent

  def number_of_modes(self):
    return 2

  def is_active(self):
    return self._parent.mode() == 1

  def update(self):
    """ NOTE: Parent mode selector determines whether 
    we want to show these selector buttons or not """
    if self.is_active(): 
      self._session.setup(as_active = False)
      for row in range(self._matrix.height()):
        for column in range(self._matrix.width()):
          self._matrix.get_button(column, row).turn_off()
      
      for index, button in enumerate(self._modes_buttons):
        if self.mode() == index:
          button.send_value(GREEN_HI)
        else:
          button.send_value(RED_HI)
    else:
      self._session.setup()
      # Actually render

  def _setup_mode_buttons(self, as_active = True):
    mode_buttons = []
    for button_index in range(self.number_of_modes()):
      mode_buttons.append(self._matrix.get_button(button_index, (self._matrix.height() - 1)))
    if as_active:
      self.set_mode_buttons(mode_buttons)
    else:
      self.set_mode_buttons(None)

  def set_mode_buttons(self, buttons):
    if buttons is None:
      for button in self._modes_buttons:
        button.remove_value_listener(self._mode_value)
      self._modes_buttons = []
    else:
      for button in buttons:
        identify_sender = True
        button.add_value_listener(self._mode_value, identify_sender)
        self._modes_buttons.append(button)
    self.update()
    # pick either session or sequencer


  def mode(self):
    return self._mode_index
