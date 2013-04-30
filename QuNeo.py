from __future__ import with_statement

import Live
import time
import math

from _Framework.ControlSurface import ControlSurface
from QuNeoSelectorComponent import QuNeoSelectorComponent
from MIDI_Map import *


class QuNeo(ControlSurface):
  """ Root class for the KMI QuNeo """

  def __init__(self, c_instance):
    ControlSurface.__init__(self, c_instance)
    with self.component_guard():
      self.setup_selector()
      #self.setup_mixer()
      #self.setup_transport()
      self.set_highlighting_session_component(self._selector._session)


  def setup_selector(self):
    self._selector = QuNeoSelectorComponent(CLIP_NOTE_MAP, SHIFT_BUTTON)
