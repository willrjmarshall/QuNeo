from _Framework.SessionComponent import SessionComponent
from QuNeoUtility import QuNeoUtility
from MIDI_Map import *

class QuNeoSessionComponent(SessionComponent, QuNeoUtility):
  """ A customized SessionComponent that can configure itself """

  def __init__(self, matrix, *a, **k):
    SessionComponent.__init__(self, self.session_width(matrix), matrix.height())
    self._matrix = matrix 
    self.setup()

  def session_width(self, matrix):
    """ The QuNeo only uses 7/8 columns for clip control """
    return (matrix.width() - 1)


  def setup(self, as_active = True):
    if as_active:
      self.set_scene_bank_buttons(
        self.button(PAD_CHANNEL, SESSION_UP),
        self.button(PAD_CHANNEL, SESSION_DOWN))

      self.set_track_bank_buttons(
        self.button(PAD_CHANNEL, SESSION_RIGHT),
        self.button(PAD_CHANNEL, SESSION_LEFT))
    else:
      self.set_scene_bank_buttons(
        None,
        None)
      self.set_track_bank_buttons(
        None,
        None)
  
    matrix = self._matrix
    for scene_index in range(matrix.height()):
      scene = self.scene(scene_index)
      if as_active:
        scene_button = matrix.get_button(7, scene_index)
        scene.set_launch_button(scene_button)
      else:
        scene.set_launch_button(None)
      for track_index in range(self.session_width(matrix)):
        clip_slot = scene.clip_slot(track_index) 
        if as_active:
          button = matrix.get_button(track_index, scene_index)
          clip_slot.set_launch_button(button)
          clip_slot.set_stopped_value(RED_HI)
        else:
          clip_slot.set_launch_button(None)
    self.update()
    
  #def setup(self, as_active = True):
    #if as_active:
      #matrix = self._matrix


      #for scene_index in range(matrix.height()):
        #scene = self.scene(scene_index)
        #if as_active:
          #scene_button = matrix.get_button(7, scene_index)
          #scene.set_launch_button(scene_button)
        #else:
          #scene.set_launch_button(None)
        #for track_index in range(self.session_width(matrix)):
          #clip_slot = scene.clip_slot(track_index) 
          #if as_active:
            #button = matrix.get_button(track_index, scene_index)
            #clip_slot.set_launch_button(button)
            #clip_slot.set_stopped_value(RED_HI)
          #else:
            #clip_slot.set_launch_button(None)
    #else:
    #self.update()


