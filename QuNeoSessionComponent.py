from _Framework.SessionComponent import SessionComponent
from QuNeoUtility import QuNeoUtility
from MIDI_Map import *

class QuNeoSessionComponent(SessionComponent, QuNeoUtility):
  """ A customized SessionComponent that can configure itself """

  def __init__(self, matrix, *a, **k):
    SessionComponent.__init__(self, self.session_width(matrix), matrix.height())
    self._matrix = matrix 
    self._clip_loop_start = None
    self._clip_loop_length = None
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

      self.set_clip_loop_start(self.encoder(SLIDER_CHANNEL, LOOP_START))
      self.set_clip_loop_length(self.encoder(SLIDER_CHANNEL, LOOP_END))

      self.set_select_buttons(
          self.button(PAD_CHANNEL, SCENE_DOWN),
          self.button(PAD_CHANNEL, SCENE_UP))

    else:
      self.set_scene_bank_buttons(
        None,
        None)
      self.set_track_bank_buttons(
        None,
        None)
      self.set_clip_loop_start(None)
      self.set_clip_loop_length(None)
      #self.set_select_buttons(None, None)

    matrix = self._matrix
    if as_active:
      stop_buttons = []
      for column in range(7):
        stop_buttons.append(matrix.get_button(column, 4))
      self.set_stop_track_clip_buttons(stop_buttons)
      self.set_stop_all_clips_button(matrix.get_button(7, 4))
    else:
      self.set_stop_track_clip_buttons([])
      self.set_stop_all_clips_button(None)

    for scene_index in range(4):
      scene = self.scene(scene_index)
      if as_active:
        scene_button = matrix.get_button(7, scene_index)
        scene.set_launch_button(scene_button)
      else:
        scene.set_launch_button(None)
      for track_index in range(self.session_width(matrix) - 1):
        clip_slot = scene.clip_slot(track_index) 
        if as_active:
          button = matrix.get_button(track_index, scene_index)
          clip_slot.set_launch_button(button)
          clip_slot.set_stopped_value(RED_HI)
        else:
          clip_slot.set_launch_button(None)
    self.update()
    
  def set_clip_loop_start(self, encoder):
    if(self._clip_loop_start != encoder):
      if (self._clip_loop_start != None):
        self._clip_loop_start.remove_value_listener(self._slot_launch_loop_value)
      self._clip_loop_start = encoder
      if (self._clip_loop_start != None):
        self._clip_loop_start.add_value_listener(self._slot_launch_loop_value)

  def set_clip_loop_length(self, encoder):
    if(self._clip_loop_length != encoder):
      if (self._clip_loop_length != None):
        self._clip_loop_length.remove_value_listener(self._clip_loop_length_value)
      self._clip_loop_length = encoder
      if (self._clip_loop_length != None):
        self._clip_loop_length.add_value_listener(self._clip_loop_length_value)

  def _slot_launch_loop_value(self, value):
  	if self.is_enabled():
  		if value != 0:
  			if value > 1:
  				new_value = -0.25
  			else:
  				new_value = 0.25
  			if (self.song().view.highlighted_clip_slot != None):
  				if self.song().view.highlighted_clip_slot.clip != None:
  					if(self.song().view.highlighted_clip_slot.clip.looping != False):
  						self.song().view.highlighted_clip_slot.clip.add_loop_start_listener
  						loop_start_pos = self.song().view.highlighted_clip_slot.clip.loop_start
  						loop_end_pos = self.song().view.highlighted_clip_slot.clip.loop_end
  						loop_length = self.song().view.highlighted_clip_slot.clip.length
  						real_value = (loop_start_pos + new_value)
  						if real_value < 0.0:
  							None
  						else:
  							self.song().view.highlighted_clip_slot.clip.loop_start = real_value
  				else:
  					None

  def _clip_loop_length_value(self, value):
  	if self.is_enabled():
  		if value != 0:
  			if value > 1:
  				new_value = -0.25
  			else:
  				new_value = 0.25
  			if (self.song().view.highlighted_clip_slot != None):
  				if (self.song().view.highlighted_clip_slot.clip != None):
  					if(self.song().view.highlighted_clip_slot.clip.looping != False):
  						self.song().view.highlighted_clip_slot.clip.add_loop_end_listener
  						loop_end_pos = self.song().view.highlighted_clip_slot.clip.loop_end
  						loop_length = self.song().view.highlighted_clip_slot.clip.length
  						real_value = (loop_end_pos + new_value)
  						if real_value < 0.25:
  							return None
  						else:
  							self.song().view.highlighted_clip_slot.clip.loop_end = real_value
  				else:
  					None

  def disconnect(self):
    SessionComponent.disconnect(self)
    if (self._clip_loop_start != None):
      self._clip_loop_start.remove_value_listener(self._slot_launch_loop_value)
      self._clip_loop_start = None
    if (self._clip_loop_length != None):
      self._clip_loop_length.remove_value_listener(self._clip_loop_length_value)
      self._clip_loop_length = None
