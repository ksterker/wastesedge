# This file was created automatically by SWIG.
import adonthellc
class gz_file:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_gz_file,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_gz_file(self)
    def open(*args):
        val = apply(adonthellc.gz_file_open,args)
        return val
    def close(*args):
        val = apply(adonthellc.gz_file_close,args)
        return val
    def is_open(*args):
        val = apply(adonthellc.gz_file_is_open,args)
        return val
    def eof(*args):
        val = apply(adonthellc.gz_file_eof,args)
        return val
    def __repr__(self):
        return "<C gz_file instance at %s>" % (self.this,)
class gz_filePtr(gz_file):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = gz_file



class igzstream(gz_file):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_igzstream,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_igzstream(self)
    def open(*args):
        val = apply(adonthellc.igzstream_open,args)
        return val
    def get_block(*args):
        val = apply(adonthellc.igzstream_get_block,args)
        return val
    def __repr__(self):
        return "<C igzstream instance at %s>" % (self.this,)
class igzstreamPtr(igzstream):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = igzstream



class ogzstream(gz_file):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_ogzstream,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_ogzstream(self)
    def open(*args):
        val = apply(adonthellc.ogzstream_open,args)
        return val
    def put_block(*args):
        val = apply(adonthellc.ogzstream_put_block,args)
        return val
    def __repr__(self):
        return "<C ogzstream instance at %s>" % (self.this,)
class ogzstreamPtr(ogzstream):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = ogzstream



class fileops:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_fileops,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_fileops(self)
    def __repr__(self):
        return "<C fileops instance at %s>" % (self.this,)
class fileopsPtr(fileops):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = fileops



class storage:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_storage,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_storage(self)
    def set(*args):
        val = apply(adonthellc.storage_set,args)
        return val
    def get(*args):
        val = apply(adonthellc.storage_get,args)
        return val
    def next(*args):
        val = apply(adonthellc.storage_next,args)
        return val
    def __repr__(self):
        return "<C storage instance at %s>" % (self.this,)
class storagePtr(storage):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = storage



class objects:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_objects,args)
        self.thisown = 1

    def set(*args):
        val = apply(adonthellc.objects_set,args)
        return val
    def get(*args):
        val = apply(adonthellc.objects_get,args)
        if val: val = storagePtr(val) 
        return val
    def erase(*args):
        val = apply(adonthellc.objects_erase,args)
        return val
    def next(*args):
        val = apply(adonthellc.objects_next,args)
        if val: val = storagePtr(val) 
        return val
    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_objects(self)
    def __repr__(self):
        return "<C objects instance at %s>" % (self.this,)
class objectsPtr(objects):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = objects



class event:
    def __init__(self,this):
        self.this = this

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_event(self)
    def script_file(*args):
        val = apply(adonthellc.event_script_file,args)
        return val
    def save(*args):
        val = apply(adonthellc.event_save,args)
        return val
    def load(*args):
        val = apply(adonthellc.event_load,args)
        return val
    def set_script(*args):
        val = apply(adonthellc.event_set_script,args)
        return val
    def __repr__(self):
        return "<C event instance at %s>" % (self.this,)
class eventPtr(event):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = event



class event_list:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_event_list,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_event_list(self)
    def clear(*args):
        val = apply(adonthellc.event_list_clear,args)
        return val
    def add_event(*args):
        val = apply(adonthellc.event_list_add_event,args)
        return val
    def save(*args):
        val = apply(adonthellc.event_list_save,args)
        return val
    def load(*args):
        val = apply(adonthellc.event_list_load,args)
        return val
    def __repr__(self):
        return "<C event_list instance at %s>" % (self.this,)
class event_listPtr(event_list):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = event_list



class event_handler:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_event_handler,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_event_handler(self)
    def __repr__(self):
        return "<C event_handler instance at %s>" % (self.this,)
class event_handlerPtr(event_handler):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = event_handler



class gametime:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_gametime,args)
        self.thisown = 1

    def tick(*args):
        val = apply(adonthellc.gametime_tick,args)
        return val
    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_gametime(self)
    def __repr__(self):
        return "<C gametime instance at %s>" % (self.this,)
class gametimePtr(gametime):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = gametime



class time_event(event):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_time_event,args)
        self.thisown = 1

    def save(*args):
        val = apply(adonthellc.time_event_save,args)
        return val
    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_time_event(self)
    __setmethods__ = {
        "minute" : adonthellc.time_event_minute_set,
        "m_step" : adonthellc.time_event_m_step_set,
        "hour" : adonthellc.time_event_hour_set,
        "h_step" : adonthellc.time_event_h_step_set,
        "day" : adonthellc.time_event_day_set,
        "d_step" : adonthellc.time_event_d_step_set,
        "time" : adonthellc.time_event_time_set,
    }
    def __setattr__(self,name,value):
        if (name == "this") or (name == "thisown"): self.__dict__[name] = value; return
        method = time_event.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value
    __getmethods__ = {
        "minute" : adonthellc.time_event_minute_get,
        "m_step" : adonthellc.time_event_m_step_get,
        "hour" : adonthellc.time_event_hour_get,
        "h_step" : adonthellc.time_event_h_step_get,
        "day" : adonthellc.time_event_day_get,
        "d_step" : adonthellc.time_event_d_step_get,
        "time" : adonthellc.time_event_time_get,
    }
    def __getattr__(self,name):
        method = time_event.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C time_event instance at %s>" % (self.this,)
class time_eventPtr(time_event):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = time_event



class input:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_input,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_input(self)
    def __repr__(self):
        return "<C input instance at %s>" % (self.this,)
class inputPtr(input):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = input



class audio:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_audio,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_audio(self)
    def __repr__(self):
        return "<C audio instance at %s>" % (self.this,)
class audioPtr(audio):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = audio



class character_base(storage):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_character_base,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_character_base(self)
    def get_name(*args):
        val = apply(adonthellc.character_base_get_name,args)
        return val
    def set_name(*args):
        val = apply(adonthellc.character_base_set_name,args)
        return val
    def get_color(*args):
        val = apply(adonthellc.character_base_get_color,args)
        return val
    def set_color(*args):
        val = apply(adonthellc.character_base_set_color,args)
        return val
    def get_dialogue(*args):
        val = apply(adonthellc.character_base_get_dialogue,args)
        return val
    def set_dialogue(*args):
        val = apply(adonthellc.character_base_set_dialogue,args)
        return val
    def get_state(*args):
        val = apply(adonthellc.character_base_get_state,args)
        return val
    def put_state(*args):
        val = apply(adonthellc.character_base_put_state,args)
        return val
    def __repr__(self):
        return "<C character_base instance at %s>" % (self.this,)
class character_basePtr(character_base):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = character_base



class drawing_area:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_drawing_area,args)
        self.thisown = 1

    def x(*args):
        val = apply(adonthellc.drawing_area_x,args)
        return val
    def y(*args):
        val = apply(adonthellc.drawing_area_y,args)
        return val
    def length(*args):
        val = apply(adonthellc.drawing_area_length,args)
        return val
    def height(*args):
        val = apply(adonthellc.drawing_area_height,args)
        return val
    def move(*args):
        val = apply(adonthellc.drawing_area_move,args)
        return val
    def resize(*args):
        val = apply(adonthellc.drawing_area_resize,args)
        return val
    def assign_drawing_area(*args):
        val = apply(adonthellc.drawing_area_assign_drawing_area,args)
        return val
    def assigned_drawing_area(*args):
        val = apply(adonthellc.drawing_area_assigned_drawing_area,args)
        if val: val = drawing_areaPtr(val) 
        return val
    def detach_drawing_area(*args):
        val = apply(adonthellc.drawing_area_detach_drawing_area,args)
        return val
    def setup_rects(*args):
        val = apply(adonthellc.drawing_area_setup_rects,args)
        return val
    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_drawing_area(self)
    def __repr__(self):
        return "<C drawing_area instance at %s>" % (self.this,)
class drawing_areaPtr(drawing_area):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = drawing_area



class quest(storage):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_quest,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_quest(self)
    def __repr__(self):
        return "<C quest instance at %s>" % (self.this,)
class questPtr(quest):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = quest



class drawable:
    def __init__(self,this):
        self.this = this

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_drawable(self)
    def length(*args):
        val = apply(adonthellc.drawable_length,args)
        return val
    def height(*args):
        val = apply(adonthellc.drawable_height,args)
        return val
    def update(*args):
        val = apply(adonthellc.drawable_update,args)
        return val
    def input_update(*args):
        val = apply(adonthellc.drawable_input_update,args)
        return val
    def draw(*args):
        val = apply(adonthellc.drawable_draw,args)
        return val
    def __repr__(self):
        return "<C drawable instance at %s>" % (self.this,)
class drawablePtr(drawable):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = drawable



class surface(drawable):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_surface,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_surface(self)
    def is_masked(*args):
        val = apply(adonthellc.surface_is_masked,args)
        return val
    def set_mask(*args):
        val = apply(adonthellc.surface_set_mask,args)
        return val
    def alpha(*args):
        val = apply(adonthellc.surface_alpha,args)
        return val
    def set_alpha(*args):
        val = apply(adonthellc.surface_set_alpha,args)
        return val
    def draw(*args):
        val = apply(adonthellc.surface_draw,args)
        return val
    def draw_part(*args):
        val = apply(adonthellc.surface_draw_part,args)
        return val
    def fillrect(*args):
        val = apply(adonthellc.surface_fillrect,args)
        return val
    def fillrect_rgb(*args):
        val = apply(adonthellc.surface_fillrect_rgb,args)
        return val
    def lock(*args):
        val = apply(adonthellc.surface_lock,args)
        return val
    def unlock(*args):
        val = apply(adonthellc.surface_unlock,args)
        return val
    def put_pix(*args):
        val = apply(adonthellc.surface_put_pix,args)
        return val
    def put_pix_rgb(*args):
        val = apply(adonthellc.surface_put_pix_rgb,args)
        return val
    def get_pix(*args):
        val = apply(adonthellc.surface_get_pix,args)
        return val
    def get_pix_rgb(*args):
        val = apply(adonthellc.surface_get_pix_rgb,args)
        return val
    def copy(*args):
        val = apply(adonthellc.surface_copy,args)
        return val
    def __repr__(self):
        return "<C surface instance at %s>" % (self.this,)
class surfacePtr(surface):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = surface



class screen:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_screen,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_screen(self)
    def __repr__(self):
        return "<C screen instance at %s>" % (self.this,)
class screenPtr(screen):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = screen



class image(surface):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_image,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_image(self)
    def resize(*args):
        val = apply(adonthellc.image_resize,args)
        return val
    def clear(*args):
        val = apply(adonthellc.image_clear,args)
        return val
    def get(*args):
        val = apply(adonthellc.image_get,args)
        return val
    def load(*args):
        val = apply(adonthellc.image_load,args)
        return val
    def get_raw(*args):
        val = apply(adonthellc.image_get_raw,args)
        return val
    def load_raw(*args):
        val = apply(adonthellc.image_load_raw,args)
        return val
    def get_pnm(*args):
        val = apply(adonthellc.image_get_pnm,args)
        return val
    def load_pnm(*args):
        val = apply(adonthellc.image_load_pnm,args)
        return val
    def put(*args):
        val = apply(adonthellc.image_put,args)
        return val
    def save(*args):
        val = apply(adonthellc.image_save,args)
        return val
    def put_raw(*args):
        val = apply(adonthellc.image_put_raw,args)
        return val
    def save_raw(*args):
        val = apply(adonthellc.image_save_raw,args)
        return val
    def put_pnm(*args):
        val = apply(adonthellc.image_put_pnm,args)
        return val
    def save_pnm(*args):
        val = apply(adonthellc.image_save_pnm,args)
        return val
    def zoom(*args):
        val = apply(adonthellc.image_zoom,args)
        return val
    def zoom_to(*args):
        val = apply(adonthellc.image_zoom_to,args)
        return val
    def tile(*args):
        val = apply(adonthellc.image_tile,args)
        return val
    def tile_to(*args):
        val = apply(adonthellc.image_tile_to,args)
        return val
    def brightness(*args):
        val = apply(adonthellc.image_brightness,args)
        return val
    def copy(*args):
        val = apply(adonthellc.image_copy,args)
        return val
    def __repr__(self):
        return "<C image instance at %s>" % (self.this,)
class imagePtr(image):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = image



class animationframe:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_animationframe,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_animationframe(self)
    def clear(*args):
        val = apply(adonthellc.animationframe_clear,args)
        return val
    def is_masked(*args):
        val = apply(adonthellc.animationframe_is_masked,args)
        return val
    def set_mask(*args):
        val = apply(adonthellc.animationframe_set_mask,args)
        return val
    def alpha(*args):
        val = apply(adonthellc.animationframe_alpha,args)
        return val
    def set_alpha(*args):
        val = apply(adonthellc.animationframe_set_alpha,args)
        return val
    def image_nbr(*args):
        val = apply(adonthellc.animationframe_image_nbr,args)
        return val
    def set_image_nbr(*args):
        val = apply(adonthellc.animationframe_set_image_nbr,args)
        return val
    def delay(*args):
        val = apply(adonthellc.animationframe_delay,args)
        return val
    def set_delay(*args):
        val = apply(adonthellc.animationframe_set_delay,args)
        return val
    def nextframe(*args):
        val = apply(adonthellc.animationframe_nextframe,args)
        return val
    def set_nextframe(*args):
        val = apply(adonthellc.animationframe_set_nextframe,args)
        return val
    def offx(*args):
        val = apply(adonthellc.animationframe_offx,args)
        return val
    def offy(*args):
        val = apply(adonthellc.animationframe_offy,args)
        return val
    def set_offset(*args):
        val = apply(adonthellc.animationframe_set_offset,args)
        return val
    def get(*args):
        val = apply(adonthellc.animationframe_get,args)
        return val
    def put(*args):
        val = apply(adonthellc.animationframe_put,args)
        return val
    def __repr__(self):
        return "<C animationframe instance at %s>" % (self.this,)
class animationframePtr(animationframe):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = animationframe



class animation(drawable):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_animation,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_animation(self)
    def clear(*args):
        val = apply(adonthellc.animation_clear,args)
        return val
    def play(*args):
        val = apply(adonthellc.animation_play,args)
        return val
    def stop(*args):
        val = apply(adonthellc.animation_stop,args)
        return val
    def playstate(*args):
        val = apply(adonthellc.animation_playstate,args)
        return val
    def rewind(*args):
        val = apply(adonthellc.animation_rewind,args)
        return val
    def next_frame(*args):
        val = apply(adonthellc.animation_next_frame,args)
        return val
    def update(*args):
        val = apply(adonthellc.animation_update,args)
        return val
    def draw(*args):
        val = apply(adonthellc.animation_draw,args)
        return val
    def get(*args):
        val = apply(adonthellc.animation_get,args)
        return val
    def load(*args):
        val = apply(adonthellc.animation_load,args)
        return val
    def put(*args):
        val = apply(adonthellc.animation_put,args)
        return val
    def save(*args):
        val = apply(adonthellc.animation_save,args)
        return val
    def nbr_of_frames(*args):
        val = apply(adonthellc.animation_nbr_of_frames,args)
        return val
    def nbr_of_images(*args):
        val = apply(adonthellc.animation_nbr_of_images,args)
        return val
    def currentframe(*args):
        val = apply(adonthellc.animation_currentframe,args)
        return val
    def set_currentframe(*args):
        val = apply(adonthellc.animation_set_currentframe,args)
        return val
    def xoffset(*args):
        val = apply(adonthellc.animation_xoffset,args)
        return val
    def yoffset(*args):
        val = apply(adonthellc.animation_yoffset,args)
        return val
    def set_offset(*args):
        val = apply(adonthellc.animation_set_offset,args)
        return val
    def get_frame(*args):
        val = apply(adonthellc.animation_get_frame,args)
        if val: val = animationframePtr(val) 
        return val
    def get_image(*args):
        val = apply(adonthellc.animation_get_image,args)
        if val: val = imagePtr(val) 
        return val
    def insert_image(*args):
        val = apply(adonthellc.animation_insert_image,args)
        return val
    def insert_frame(*args):
        val = apply(adonthellc.animation_insert_frame,args)
        return val
    def delete_image(*args):
        val = apply(adonthellc.animation_delete_image,args)
        return val
    def delete_frame(*args):
        val = apply(adonthellc.animation_delete_frame,args)
        return val
    def zoom(*args):
        val = apply(adonthellc.animation_zoom,args)
        return val
    def copy(*args):
        val = apply(adonthellc.animation_copy,args)
        return val
    def __repr__(self):
        return "<C animation instance at %s>" % (self.this,)
class animationPtr(animation):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = animation



class mapsquare_walkable:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_mapsquare_walkable,args)
        self.thisown = 1

    def get(*args):
        val = apply(adonthellc.mapsquare_walkable_get,args)
        return val
    def put(*args):
        val = apply(adonthellc.mapsquare_walkable_put,args)
        return val
    def is_walkable_west(*args):
        val = apply(adonthellc.mapsquare_walkable_is_walkable_west,args)
        return val
    def is_walkable_east(*args):
        val = apply(adonthellc.mapsquare_walkable_is_walkable_east,args)
        return val
    def is_walkable_north(*args):
        val = apply(adonthellc.mapsquare_walkable_is_walkable_north,args)
        return val
    def is_walkable_south(*args):
        val = apply(adonthellc.mapsquare_walkable_is_walkable_south,args)
        return val
    def set_walkable_west(*args):
        val = apply(adonthellc.mapsquare_walkable_set_walkable_west,args)
        return val
    def set_walkable_east(*args):
        val = apply(adonthellc.mapsquare_walkable_set_walkable_east,args)
        return val
    def set_walkable_north(*args):
        val = apply(adonthellc.mapsquare_walkable_set_walkable_north,args)
        return val
    def set_walkable_south(*args):
        val = apply(adonthellc.mapsquare_walkable_set_walkable_south,args)
        return val
    def get_walkable(*args):
        val = apply(adonthellc.mapsquare_walkable_get_walkable,args)
        return val
    def set_walkable(*args):
        val = apply(adonthellc.mapsquare_walkable_set_walkable,args)
        return val
    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_mapsquare_walkable(self)
    def __repr__(self):
        return "<C mapsquare_walkable instance at %s>" % (self.this,)
class mapsquare_walkablePtr(mapsquare_walkable):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = mapsquare_walkable



class mapsquare_walkable_area(drawable):
    def __init__(self,this):
        self.this = this

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_mapsquare_walkable_area(self)
    def clear(*args):
        val = apply(adonthellc.mapsquare_walkable_area_clear,args)
        return val
    def draw(*args):
        val = apply(adonthellc.mapsquare_walkable_area_draw,args)
        return val
    def area_length(*args):
        val = apply(adonthellc.mapsquare_walkable_area_area_length,args)
        return val
    def area_height(*args):
        val = apply(adonthellc.mapsquare_walkable_area_area_height,args)
        return val
    def get_square(*args):
        val = apply(adonthellc.mapsquare_walkable_area_get_square,args)
        if val: val = mapsquare_walkablePtr(val) 
        return val
    def resize_area(*args):
        val = apply(adonthellc.mapsquare_walkable_area_resize_area,args)
        return val
    def base_x(*args):
        val = apply(adonthellc.mapsquare_walkable_area_base_x,args)
        return val
    def base_y(*args):
        val = apply(adonthellc.mapsquare_walkable_area_base_y,args)
        return val
    def set_base(*args):
        val = apply(adonthellc.mapsquare_walkable_area_set_base,args)
        return val
    def get(*args):
        val = apply(adonthellc.mapsquare_walkable_area_get,args)
        return val
    def put(*args):
        val = apply(adonthellc.mapsquare_walkable_area_put,args)
        return val
    def copy(*args):
        val = apply(adonthellc.mapsquare_walkable_area_copy,args)
        return val
    def __repr__(self):
        return "<C mapsquare_walkable_area instance at %s>" % (self.this,)
class mapsquare_walkable_areaPtr(mapsquare_walkable_area):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = mapsquare_walkable_area



class mapsquare_tile:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_mapsquare_tile,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_mapsquare_tile(self)
    def __repr__(self):
        return "<C mapsquare_tile instance at %s>" % (self.this,)
class mapsquare_tilePtr(mapsquare_tile):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = mapsquare_tile



class mapsquare_char:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_mapsquare_char,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_mapsquare_char(self)
    def __repr__(self):
        return "<C mapsquare_char instance at %s>" % (self.this,)
class mapsquare_charPtr(mapsquare_char):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = mapsquare_char



class mapsquare(mapsquare_walkable):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_mapsquare,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_mapsquare(self)
    def is_free(*args):
        val = apply(adonthellc.mapsquare_is_free,args)
        return val
    def whoshere(*args):
        val = apply(adonthellc.mapsquare_whoshere,args)
        if val: val = mapcharacterPtr(val) 
        return val
    def __repr__(self):
        return "<C mapsquare instance at %s>" % (self.this,)
class mapsquarePtr(mapsquare):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = mapsquare



class mapsquare_area:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_mapsquare_area,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_mapsquare_area(self)
    def clear(*args):
        val = apply(adonthellc.mapsquare_area_clear,args)
        return val
    def area_length(*args):
        val = apply(adonthellc.mapsquare_area_area_length,args)
        return val
    def area_height(*args):
        val = apply(adonthellc.mapsquare_area_area_height,args)
        return val
    def get_square(*args):
        val = apply(adonthellc.mapsquare_area_get_square,args)
        if val: val = mapsquarePtr(val) 
        return val
    def resize_area(*args):
        val = apply(adonthellc.mapsquare_area_resize_area,args)
        return val
    def __repr__(self):
        return "<C mapsquare_area instance at %s>" % (self.this,)
class mapsquare_areaPtr(mapsquare_area):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = mapsquare_area



class mapobject(mapsquare_walkable_area):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_mapobject,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_mapobject(self)
    def clear(*args):
        val = apply(adonthellc.mapobject_clear,args)
        return val
    def update(*args):
        val = apply(adonthellc.mapobject_update,args)
        return val
    def draw(*args):
        val = apply(adonthellc.mapobject_draw,args)
        return val
    def draw_from_base(*args):
        val = apply(adonthellc.mapobject_draw_from_base,args)
        return val
    def get(*args):
        val = apply(adonthellc.mapobject_get,args)
        return val
    def load(*args):
        val = apply(adonthellc.mapobject_load,args)
        return val
    def put(*args):
        val = apply(adonthellc.mapobject_put,args)
        return val
    def save(*args):
        val = apply(adonthellc.mapobject_save,args)
        return val
    def nbr_of_animations(*args):
        val = apply(adonthellc.mapobject_nbr_of_animations,args)
        return val
    def get_animation(*args):
        val = apply(adonthellc.mapobject_get_animation,args)
        if val: val = animationPtr(val) 
        return val
    def insert_animation(*args):
        val = apply(adonthellc.mapobject_insert_animation,args)
        return val
    def delete_animation(*args):
        val = apply(adonthellc.mapobject_delete_animation,args)
        return val
    def copy(*args):
        val = apply(adonthellc.mapobject_copy,args)
        return val
    def __repr__(self):
        return "<C mapobject instance at %s>" % (self.this,)
class mapobjectPtr(mapobject):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = mapobject



class mapcharacter(mapsquare_walkable_area,character_base):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_mapcharacter,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_mapcharacter(self)
    def clear(*args):
        val = apply(adonthellc.mapcharacter_clear,args)
        return val
    def filename(*args):
        val = apply(adonthellc.mapcharacter_filename,args)
        return val
    def update(*args):
        val = apply(adonthellc.mapcharacter_update,args)
        return val
    def draw(*args):
        val = apply(adonthellc.mapcharacter_draw,args)
        return val
    def get(*args):
        val = apply(adonthellc.mapcharacter_get,args)
        return val
    def load(*args):
        val = apply(adonthellc.mapcharacter_load,args)
        return val
    def get_state(*args):
        val = apply(adonthellc.mapcharacter_get_state,args)
        return val
    def put_state(*args):
        val = apply(adonthellc.mapcharacter_put_state,args)
        return val
    def set_map(*args):
        val = apply(adonthellc.mapcharacter_set_map,args)
        return val
    def remove_from_map(*args):
        val = apply(adonthellc.mapcharacter_remove_from_map,args)
        return val
    def mymap(*args):
        val = apply(adonthellc.mapcharacter_mymap,args)
        if val: val = landmapPtr(val) 
        return val
    def stand_north(*args):
        val = apply(adonthellc.mapcharacter_stand_north,args)
        return val
    def stand_south(*args):
        val = apply(adonthellc.mapcharacter_stand_south,args)
        return val
    def stand_east(*args):
        val = apply(adonthellc.mapcharacter_stand_east,args)
        return val
    def stand_west(*args):
        val = apply(adonthellc.mapcharacter_stand_west,args)
        return val
    def stand(*args):
        val = apply(adonthellc.mapcharacter_stand,args)
        return val
    def go_north(*args):
        val = apply(adonthellc.mapcharacter_go_north,args)
        return val
    def go_south(*args):
        val = apply(adonthellc.mapcharacter_go_south,args)
        return val
    def go_east(*args):
        val = apply(adonthellc.mapcharacter_go_east,args)
        return val
    def go_west(*args):
        val = apply(adonthellc.mapcharacter_go_west,args)
        return val
    def can_go_north(*args):
        val = apply(adonthellc.mapcharacter_can_go_north,args)
        return val
    def can_go_south(*args):
        val = apply(adonthellc.mapcharacter_can_go_south,args)
        return val
    def can_go_east(*args):
        val = apply(adonthellc.mapcharacter_can_go_east,args)
        return val
    def can_go_west(*args):
        val = apply(adonthellc.mapcharacter_can_go_west,args)
        return val
    def look_invert(*args):
        val = apply(adonthellc.mapcharacter_look_invert,args)
        return val
    def whosnext(*args):
        val = apply(adonthellc.mapcharacter_whosnext,args)
        if val: val = mapcharacterPtr(val) 
        return val
    def set_offset(*args):
        val = apply(adonthellc.mapcharacter_set_offset,args)
        return val
    def remove_from_pos(*args):
        val = apply(adonthellc.mapcharacter_remove_from_pos,args)
        return val
    def jump_to(*args):
        val = apply(adonthellc.mapcharacter_jump_to,args)
        return val
    def submap(*args):
        val = apply(adonthellc.mapcharacter_submap,args)
        return val
    def posx(*args):
        val = apply(adonthellc.mapcharacter_posx,args)
        return val
    def posy(*args):
        val = apply(adonthellc.mapcharacter_posy,args)
        return val
    def offx(*args):
        val = apply(adonthellc.mapcharacter_offx,args)
        return val
    def offy(*args):
        val = apply(adonthellc.mapcharacter_offy,args)
        return val
    def currentmove(*args):
        val = apply(adonthellc.mapcharacter_currentmove,args)
        return val
    def set_schedule(*args):
        val = apply(adonthellc.mapcharacter_set_schedule,args)
        return val
    def schedule_file(*args):
        val = apply(adonthellc.mapcharacter_schedule_file,args)
        return val
    def is_schedule_activated(*args):
        val = apply(adonthellc.mapcharacter_is_schedule_activated,args)
        return val
    def set_schedule_active(*args):
        val = apply(adonthellc.mapcharacter_set_schedule_active,args)
        return val
    def set_action(*args):
        val = apply(adonthellc.mapcharacter_set_action,args)
        return val
    def action_file(*args):
        val = apply(adonthellc.mapcharacter_action_file,args)
        return val
    def is_action_activated(*args):
        val = apply(adonthellc.mapcharacter_is_action_activated,args)
        return val
    def set_action_active(*args):
        val = apply(adonthellc.mapcharacter_set_action_active,args)
        return val
    def launch_action(*args):
        val = apply(adonthellc.mapcharacter_launch_action,args)
        return val
    def copy(*args):
        val = apply(adonthellc.mapcharacter_copy,args)
        return val
    def __repr__(self):
        return "<C mapcharacter instance at %s>" % (self.this,)
class mapcharacterPtr(mapcharacter):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = mapcharacter



class character(mapcharacter):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_character,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_character(self)
    def __repr__(self):
        return "<C character instance at %s>" % (self.this,)
class characterPtr(character):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = character



class base_map_event(event):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_base_map_event,args)
        self.thisown = 1

    def save(*args):
        val = apply(adonthellc.base_map_event_save,args)
        return val
    def load(*args):
        val = apply(adonthellc.base_map_event_load,args)
        return val
    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_base_map_event(self)
    __setmethods__ = {
        "submap" : adonthellc.base_map_event_submap_set,
        "x" : adonthellc.base_map_event_x_set,
        "y" : adonthellc.base_map_event_y_set,
        "dir" : adonthellc.base_map_event_dir_set,
        "map" : adonthellc.base_map_event_map_set,
        "c" : adonthellc.base_map_event_c_set,
    }
    def __setattr__(self,name,value):
        if (name == "this") or (name == "thisown"): self.__dict__[name] = value; return
        method = base_map_event.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value
    __getmethods__ = {
        "submap" : adonthellc.base_map_event_submap_get,
        "x" : adonthellc.base_map_event_x_get,
        "y" : adonthellc.base_map_event_y_get,
        "dir" : adonthellc.base_map_event_dir_get,
        "map" : adonthellc.base_map_event_map_get,
        "c" : lambda x : mapcharacterPtr(adonthellc.base_map_event_c_get(x)),
    }
    def __getattr__(self,name):
        method = base_map_event.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C base_map_event instance at %s>" % (self.this,)
class base_map_eventPtr(base_map_event):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = base_map_event



class enter_event(base_map_event):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_enter_event,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_enter_event(self)
    __setmethods__ = {
        "submap" : adonthellc.enter_event_submap_set,
        "x" : adonthellc.enter_event_x_set,
        "y" : adonthellc.enter_event_y_set,
        "dir" : adonthellc.enter_event_dir_set,
        "map" : adonthellc.enter_event_map_set,
        "c" : adonthellc.enter_event_c_set,
    }
    def __setattr__(self,name,value):
        if (name == "this") or (name == "thisown"): self.__dict__[name] = value; return
        method = enter_event.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value
    __getmethods__ = {
        "submap" : adonthellc.enter_event_submap_get,
        "x" : adonthellc.enter_event_x_get,
        "y" : adonthellc.enter_event_y_get,
        "dir" : adonthellc.enter_event_dir_get,
        "map" : adonthellc.enter_event_map_get,
        "c" : lambda x : mapcharacterPtr(adonthellc.enter_event_c_get(x)),
    }
    def __getattr__(self,name):
        method = enter_event.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C enter_event instance at %s>" % (self.this,)
class enter_eventPtr(enter_event):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = enter_event



class leave_event(base_map_event):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_leave_event,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_leave_event(self)
    __setmethods__ = {
        "submap" : adonthellc.leave_event_submap_set,
        "x" : adonthellc.leave_event_x_set,
        "y" : adonthellc.leave_event_y_set,
        "dir" : adonthellc.leave_event_dir_set,
        "map" : adonthellc.leave_event_map_set,
        "c" : adonthellc.leave_event_c_set,
    }
    def __setattr__(self,name,value):
        if (name == "this") or (name == "thisown"): self.__dict__[name] = value; return
        method = leave_event.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value
    __getmethods__ = {
        "submap" : adonthellc.leave_event_submap_get,
        "x" : adonthellc.leave_event_x_get,
        "y" : adonthellc.leave_event_y_get,
        "dir" : adonthellc.leave_event_dir_get,
        "map" : adonthellc.leave_event_map_get,
        "c" : lambda x : mapcharacterPtr(adonthellc.leave_event_c_get(x)),
    }
    def __getattr__(self,name):
        method = leave_event.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C leave_event instance at %s>" % (self.this,)
class leave_eventPtr(leave_event):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = leave_event



class landmap(event_list):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_landmap,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_landmap(self)
    def clear(*args):
        val = apply(adonthellc.landmap_clear,args)
        return val
    def nbr_of_mapobjects(*args):
        val = apply(adonthellc.landmap_nbr_of_mapobjects,args)
        return val
    def nbr_of_submaps(*args):
        val = apply(adonthellc.landmap_nbr_of_submaps,args)
        return val
    def nbr_of_mapcharacters(*args):
        val = apply(adonthellc.landmap_nbr_of_mapcharacters,args)
        return val
    def filename(*args):
        val = apply(adonthellc.landmap_filename,args)
        return val
    def get_mapcharacter(*args):
        val = apply(adonthellc.landmap_get_mapcharacter,args)
        if val: val = mapcharacterPtr(val) 
        return val
    def get_mapobject(*args):
        val = apply(adonthellc.landmap_get_mapobject,args)
        if val: val = mapobjectPtr(val) 
        return val
    def get_submap(*args):
        val = apply(adonthellc.landmap_get_submap,args)
        if val: val = mapsquare_areaPtr(val) 
        return val
    def update(*args):
        val = apply(adonthellc.landmap_update,args)
        return val
    def get(*args):
        val = apply(adonthellc.landmap_get,args)
        return val
    def load(*args):
        val = apply(adonthellc.landmap_load,args)
        return val
    def put(*args):
        val = apply(adonthellc.landmap_put,args)
        return val
    def save(*args):
        val = apply(adonthellc.landmap_save,args)
        return val
    def get_state(*args):
        val = apply(adonthellc.landmap_get_state,args)
        return val
    def put_state(*args):
        val = apply(adonthellc.landmap_put_state,args)
        return val
    def put_mapobject(*args):
        val = apply(adonthellc.landmap_put_mapobject,args)
        return val
    def remove_mapobject(*args):
        val = apply(adonthellc.landmap_remove_mapobject,args)
        return val
    def insert_submap(*args):
        val = apply(adonthellc.landmap_insert_submap,args)
        return val
    def delete_submap(*args):
        val = apply(adonthellc.landmap_delete_submap,args)
        return val
    def insert_mapobject(*args):
        val = apply(adonthellc.landmap_insert_mapobject,args)
        return val
    def delete_mapobject(*args):
        val = apply(adonthellc.landmap_delete_mapobject,args)
        return val
    def __repr__(self):
        return "<C landmap instance at %s>" % (self.this,)
class landmapPtr(landmap):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = landmap



class mapview(drawable):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_mapview,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_mapview(self)
    def attach_map(*args):
        val = apply(adonthellc.mapview_attach_map,args)
        return val
    def detach_map(*args):
        val = apply(adonthellc.mapview_detach_map,args)
        return val
    def set_pos(*args):
        val = apply(adonthellc.mapview_set_pos,args)
        return val
    def center_on(*args):
        val = apply(adonthellc.mapview_center_on,args)
        return val
    def currentsubmap(*args):
        val = apply(adonthellc.mapview_currentsubmap,args)
        return val
    def posx(*args):
        val = apply(adonthellc.mapview_posx,args)
        return val
    def posy(*args):
        val = apply(adonthellc.mapview_posy,args)
        return val
    def offx(*args):
        val = apply(adonthellc.mapview_offx,args)
        return val
    def offy(*args):
        val = apply(adonthellc.mapview_offy,args)
        return val
    def can_scroll_right(*args):
        val = apply(adonthellc.mapview_can_scroll_right,args)
        return val
    def can_scroll_left(*args):
        val = apply(adonthellc.mapview_can_scroll_left,args)
        return val
    def can_scroll_up(*args):
        val = apply(adonthellc.mapview_can_scroll_up,args)
        return val
    def can_scroll_down(*args):
        val = apply(adonthellc.mapview_can_scroll_down,args)
        return val
    def scroll_right(*args):
        val = apply(adonthellc.mapview_scroll_right,args)
        return val
    def scroll_left(*args):
        val = apply(adonthellc.mapview_scroll_left,args)
        return val
    def scroll_down(*args):
        val = apply(adonthellc.mapview_scroll_down,args)
        return val
    def scroll_up(*args):
        val = apply(adonthellc.mapview_scroll_up,args)
        return val
    def get_state(*args):
        val = apply(adonthellc.mapview_get_state,args)
        return val
    def put_state(*args):
        val = apply(adonthellc.mapview_put_state,args)
        return val
    def resize(*args):
        val = apply(adonthellc.mapview_resize,args)
        return val
    def set_schedule(*args):
        val = apply(adonthellc.mapview_set_schedule,args)
        return val
    def schedule_file(*args):
        val = apply(adonthellc.mapview_schedule_file,args)
        return val
    def update(*args):
        val = apply(adonthellc.mapview_update,args)
        return val
    def draw(*args):
        val = apply(adonthellc.mapview_draw,args)
        return val
    def __repr__(self):
        return "<C mapview instance at %s>" % (self.this,)
class mapviewPtr(mapview):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = mapview



class mapengine:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_mapengine,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_mapengine(self)
    def set_mapview_schedule(*args):
        val = apply(adonthellc.mapengine_set_mapview_schedule,args)
        return val
    def load_map(*args):
        val = apply(adonthellc.mapengine_load_map,args)
        return val
    def get_landmap(*args):
        val = apply(adonthellc.mapengine_get_landmap,args)
        if val: val = landmapPtr(val) 
        return val
    def run(*args):
        val = apply(adonthellc.mapengine_run,args)
        return val
    def quit(*args):
        val = apply(adonthellc.mapengine_quit,args)
        return val
    def get_state(*args):
        val = apply(adonthellc.mapengine_get_state,args)
        return val
    def put_state(*args):
        val = apply(adonthellc.mapengine_put_state,args)
        return val
    def mainloop(*args):
        val = apply(adonthellc.mapengine_mainloop,args)
        return val
    def draw(*args):
        val = apply(adonthellc.mapengine_draw,args)
        return val
    def __repr__(self):
        return "<C mapengine instance at %s>" % (self.this,)
class mapenginePtr(mapengine):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = mapengine



class win_font:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_win_font,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_win_font(self)
    def load(*args):
        val = apply(adonthellc.win_font_load,args)
        return val
    def load_font(*args):
        val = apply(adonthellc.win_font_load_font,args)
        return val
    def in_table(*args):
        val = apply(adonthellc.win_font_in_table,args)
        return val
    def height(*args):
        val = apply(adonthellc.win_font_height,args)
        return val
    def length(*args):
        val = apply(adonthellc.win_font_length,args)
        return val
    __setmethods__ = {
        "cursor" : adonthellc.win_font_cursor_set,
    }
    def __setattr__(self,name,value):
        if (name == "this") or (name == "thisown"): self.__dict__[name] = value; return
        method = win_font.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value
    __getmethods__ = {
        "cursor" : lambda x : imagePtr(adonthellc.win_font_cursor_get(x)),
    }
    def __getattr__(self,name):
        method = win_font.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C win_font instance at %s>" % (self.this,)
class win_fontPtr(win_font):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = win_font



class win_theme:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_win_theme,args)
        self.thisown = 1

    def destroy(*args):
        val = apply(adonthellc.win_theme_destroy,args)
        return val
    def update(*args):
        val = apply(adonthellc.win_theme_update,args)
        return val
    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_win_theme(self)
    __setmethods__ = {
        "normal" : adonthellc.win_theme_normal_set,
        "mini" : adonthellc.win_theme_mini_set,
        "background" : adonthellc.win_theme_background_set,
        "scrollbar" : adonthellc.win_theme_scrollbar_set,
    }
    def __setattr__(self,name,value):
        if (name == "this") or (name == "thisown"): self.__dict__[name] = value; return
        method = win_theme.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value
    __getmethods__ = {
        "normal" : lambda x : win_borderPtr(adonthellc.win_theme_normal_get(x)),
        "mini" : lambda x : win_borderPtr(adonthellc.win_theme_mini_get(x)),
        "background" : lambda x : win_backgroundPtr(adonthellc.win_theme_background_get(x)),
        "scrollbar" : lambda x : win_scrollbarPtr(adonthellc.win_theme_scrollbar_get(x)),
    }
    def __getattr__(self,name):
        method = win_theme.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C win_theme instance at %s>" % (self.this,)
class win_themePtr(win_theme):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = win_theme



class win_base:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_win_base,args)
        self.thisown = 1

    def x(*args):
        val = apply(adonthellc.win_base_x,args)
        return val
    def y(*args):
        val = apply(adonthellc.win_base_y,args)
        return val
    def length(*args):
        val = apply(adonthellc.win_base_length,args)
        return val
    def height(*args):
        val = apply(adonthellc.win_base_height,args)
        return val
    def padx(*args):
        val = apply(adonthellc.win_base_padx,args)
        return val
    def pady(*args):
        val = apply(adonthellc.win_base_pady,args)
        return val
    def realx(*args):
        val = apply(adonthellc.win_base_realx,args)
        return val
    def realy(*args):
        val = apply(adonthellc.win_base_realy,args)
        return val
    def move(*args):
        val = apply(adonthellc.win_base_move,args)
        return val
    def resize(*args):
        val = apply(adonthellc.win_base_resize,args)
        return val
    def set_border_size(*args):
        val = apply(adonthellc.win_base_set_border_size,args)
        return val
    def set_align(*args):
        val = apply(adonthellc.win_base_set_align,args)
        return val
    def align(*args):
        val = apply(adonthellc.win_base_align,args)
        return val
    def set_visible(*args):
        val = apply(adonthellc.win_base_set_visible,args)
        return val
    def is_visible(*args):
        val = apply(adonthellc.win_base_is_visible,args)
        return val
    def set_background_visible(*args):
        val = apply(adonthellc.win_base_set_background_visible,args)
        return val
    def is_background_visible(*args):
        val = apply(adonthellc.win_base_is_background_visible,args)
        return val
    def set_border_visible(*args):
        val = apply(adonthellc.win_base_set_border_visible,args)
        return val
    def is_border_visible(*args):
        val = apply(adonthellc.win_base_is_border_visible,args)
        return val
    def set_return_code(*args):
        val = apply(adonthellc.win_base_set_return_code,args)
        return val
    def py_signal_connect(*args):
        val = apply(adonthellc.win_base_py_signal_connect,args)
        return val
    def is_can_be_selected(*args):
        val = apply(adonthellc.win_base_is_can_be_selected,args)
        return val
    def set_can_be_selected(*args):
        val = apply(adonthellc.win_base_set_can_be_selected,args)
        return val
    def is_in_select(*args):
        val = apply(adonthellc.win_base_is_in_select,args)
        return val
    def is_select(*args):
        val = apply(adonthellc.win_base_is_select,args)
        return val
    def set_activated(*args):
        val = apply(adonthellc.win_base_set_activated,args)
        return val
    def is_activated(*args):
        val = apply(adonthellc.win_base_is_activated,args)
        return val
    def is_focus(*args):
        val = apply(adonthellc.win_base_is_focus,args)
        return val
    def set_focus(*args):
        val = apply(adonthellc.win_base_set_focus,args)
        return val
    def set_draw_brightness(*args):
        val = apply(adonthellc.win_base_set_draw_brightness,args)
        return val
    def set_level_brightness(*args):
        val = apply(adonthellc.win_base_set_level_brightness,args)
        return val
    def set_level_trans_background(*args):
        val = apply(adonthellc.win_base_set_level_trans_background,args)
        return val
    def set_theme(*args):
        val = apply(adonthellc.win_base_set_theme,args)
        return val
    def get_drawing_area(*args):
        val = apply(adonthellc.win_base_get_drawing_area,args)
        if val: val = drawing_areaPtr(val) 
        return val
    def update(*args):
        val = apply(adonthellc.win_base_update,args)
        return val
    def update_real_position(*args):
        val = apply(adonthellc.win_base_update_real_position,args)
        return val
    def draw(*args):
        val = apply(adonthellc.win_base_draw,args)
        return val
    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_win_base(self)
    def __repr__(self):
        return "<C win_base instance at %s>" % (self.this,)
class win_basePtr(win_base):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = win_base



class win_container(win_base):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_win_container,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_win_container(self)
    def add(*args):
        val = apply(adonthellc.win_container_add,args)
        return val
    def remove(*args):
        val = apply(adonthellc.win_container_remove,args)
        return val
    def remove_all(*args):
        val = apply(adonthellc.win_container_remove_all,args)
        return val
    def destroy(*args):
        val = apply(adonthellc.win_container_destroy,args)
        return val
    def update(*args):
        val = apply(adonthellc.win_container_update,args)
        return val
    def draw(*args):
        val = apply(adonthellc.win_container_draw,args)
        return val
    def move(*args):
        val = apply(adonthellc.win_container_move,args)
        return val
    def resize(*args):
        val = apply(adonthellc.win_container_resize,args)
        return val
    def set_space_between_border(*args):
        val = apply(adonthellc.win_container_set_space_between_border,args)
        return val
    def set_space_between_object(*args):
        val = apply(adonthellc.win_container_set_space_between_object,args)
        return val
    def space_between_border(*args):
        val = apply(adonthellc.win_container_space_between_border,args)
        return val
    def space_between_object(*args):
        val = apply(adonthellc.win_container_space_between_object,args)
        return val
    def set_draw_brightness(*args):
        val = apply(adonthellc.win_container_set_draw_brightness,args)
        return val
    def set_visible_all(*args):
        val = apply(adonthellc.win_container_set_visible_all,args)
        return val
    def set_align_all(*args):
        val = apply(adonthellc.win_container_set_align_all,args)
        return val
    def set_layout(*args):
        val = apply(adonthellc.win_container_set_layout,args)
        return val
    def update_real_position(*args):
        val = apply(adonthellc.win_container_update_real_position,args)
        return val
    def set_focus(*args):
        val = apply(adonthellc.win_container_set_focus,args)
        return val
    def is_focus(*args):
        val = apply(adonthellc.win_container_is_focus,args)
        return val
    def __repr__(self):
        return "<C win_container instance at %s>" % (self.this,)
class win_containerPtr(win_container):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = win_container



class win_label(win_base):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_win_label,args)
        self.thisown = 1

    def draw(*args):
        val = apply(adonthellc.win_label_draw,args)
        return val
    def set_text(*args):
        val = apply(adonthellc.win_label_set_text,args)
        return val
    def add_text(*args):
        val = apply(adonthellc.win_label_add_text,args)
        return val
    def is_auto_size(*args):
        val = apply(adonthellc.win_label_is_auto_size,args)
        return val
    def is_auto_height(*args):
        val = apply(adonthellc.win_label_is_auto_height,args)
        return val
    def set_auto_size(*args):
        val = apply(adonthellc.win_label_set_auto_size,args)
        return val
    def set_auto_height(*args):
        val = apply(adonthellc.win_label_set_auto_height,args)
        return val
    def resize(*args):
        val = apply(adonthellc.win_label_resize,args)
        return val
    def update(*args):
        val = apply(adonthellc.win_label_update,args)
        return val
    def set_cursor_blinking(*args):
        val = apply(adonthellc.win_label_set_cursor_blinking,args)
        return val
    def is_cursor_blinking(*args):
        val = apply(adonthellc.win_label_is_cursor_blinking,args)
        return val
    def set_cursor_blinking_speed(*args):
        val = apply(adonthellc.win_label_set_cursor_blinking_speed,args)
        return val
    def get_text(*args):
        val = apply(adonthellc.win_label_get_text,args)
        return val
    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_win_label(self)
    def __repr__(self):
        return "<C win_label instance at %s>" % (self.this,)
class win_labelPtr(win_label):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = win_label



class win_image(win_base):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_win_image,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_win_image(self)
    def resize(*args):
        val = apply(adonthellc.win_image_resize,args)
        return val
    def set_image(*args):
        val = apply(adonthellc.win_image_set_image,args)
        return val
    def draw(*args):
        val = apply(adonthellc.win_image_draw,args)
        return val
    def set_stretch(*args):
        val = apply(adonthellc.win_image_set_stretch,args)
        return val
    def is_stretch(*args):
        val = apply(adonthellc.win_image_is_stretch,args)
        return val
    def __repr__(self):
        return "<C win_image instance at %s>" % (self.this,)
class win_imagePtr(win_image):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = win_image



class win_scrolled(win_container):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_win_scrolled,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_win_scrolled(self)
    def up(*args):
        val = apply(adonthellc.win_scrolled_up,args)
        return val
    def down(*args):
        val = apply(adonthellc.win_scrolled_down,args)
        return val
    def amplitude(*args):
        val = apply(adonthellc.win_scrolled_amplitude,args)
        return val
    def add(*args):
        val = apply(adonthellc.win_scrolled_add,args)
        return val
    def remove(*args):
        val = apply(adonthellc.win_scrolled_remove,args)
        return val
    def remove_all(*args):
        val = apply(adonthellc.win_scrolled_remove_all,args)
        return val
    def resize(*args):
        val = apply(adonthellc.win_scrolled_resize,args)
        return val
    def destroy(*args):
        val = apply(adonthellc.win_scrolled_destroy,args)
        return val
    def draw(*args):
        val = apply(adonthellc.win_scrolled_draw,args)
        return val
    def update(*args):
        val = apply(adonthellc.win_scrolled_update,args)
        return val
    def set_space_between_border(*args):
        val = apply(adonthellc.win_scrolled_set_space_between_border,args)
        return val
    def set_space_between_object(*args):
        val = apply(adonthellc.win_scrolled_set_space_between_object,args)
        return val
    def set_scrollbar_visible(*args):
        val = apply(adonthellc.win_scrolled_set_scrollbar_visible,args)
        return val
    def is_scrollbar_visible(*args):
        val = apply(adonthellc.win_scrolled_is_scrollbar_visible,args)
        return val
    def __repr__(self):
        return "<C win_scrolled instance at %s>" % (self.this,)
class win_scrolledPtr(win_scrolled):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = win_scrolled



class win_select(win_scrolled):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_win_select,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_win_select(self)
    def add(*args):
        val = apply(adonthellc.win_select_add,args)
        return val
    def remove(*args):
        val = apply(adonthellc.win_select_remove,args)
        return val
    def remove_all(*args):
        val = apply(adonthellc.win_select_remove_all,args)
        return val
    def destroy(*args):
        val = apply(adonthellc.win_select_destroy,args)
        return val
    def update(*args):
        val = apply(adonthellc.win_select_update,args)
        return val
    def get(*args):
        val = apply(adonthellc.win_select_get,args)
        if val: val = win_basePtr(val) 
        return val
    def get_pos(*args):
        val = apply(adonthellc.win_select_get_pos,args)
        return val
    def set_default(*args):
        val = apply(adonthellc.win_select_set_default,args)
        return val
    def set_can_be_selected_all(*args):
        val = apply(adonthellc.win_select_set_can_be_selected_all,args)
        return val
    def set_type(*args):
        val = apply(adonthellc.win_select_set_type,args)
        return val
    def type(*args):
        val = apply(adonthellc.win_select_type,args)
        return val
    def set_select_mode(*args):
        val = apply(adonthellc.win_select_set_select_mode,args)
        return val
    def set_select_circle(*args):
        val = apply(adonthellc.win_select_set_select_circle,args)
        return val
    def is_select_circle(*args):
        val = apply(adonthellc.win_select_is_select_circle,args)
        return val
    def __repr__(self):
        return "<C win_select instance at %s>" % (self.this,)
class win_selectPtr(win_select):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = win_select



class win_manager:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_win_manager,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_win_manager(self)
    def __repr__(self):
        return "<C win_manager instance at %s>" % (self.this,)
class win_managerPtr(win_manager):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = win_manager



class dialog_engine(win_container):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_dialog_engine,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_dialog_engine(self)
    def init(*args):
        val = apply(adonthellc.dialog_engine_init,args)
        return val
    def set_portrait(*args):
        val = apply(adonthellc.dialog_engine_set_portrait,args)
        return val
    def set_name(*args):
        val = apply(adonthellc.dialog_engine_set_name,args)
        return val
    def set_npc(*args):
        val = apply(adonthellc.dialog_engine_set_npc,args)
        return val
    def update(*args):
        val = apply(adonthellc.dialog_engine_update,args)
        return val
    def run(*args):
        val = apply(adonthellc.dialog_engine_run,args)
        return val
    def __repr__(self):
        return "<C dialog_engine instance at %s>" % (self.this,)
class dialog_enginePtr(dialog_engine):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = dialog_engine



class data_screen(win_container):
    def __init__(self,*args):
        self.this = apply(adonthellc.new_data_screen,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_data_screen(self)
    def update(*args):
        val = apply(adonthellc.data_screen_update,args)
        return val
    def __repr__(self):
        return "<C data_screen instance at %s>" % (self.this,)
class data_screenPtr(data_screen):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = data_screen



class gamedata:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_gamedata,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_gamedata(self)
    def put(*args):
        val = apply(adonthellc.gamedata_put,args)
        return val
    def get(*args):
        val = apply(adonthellc.gamedata_get,args)
        return val
    def directory(*args):
        val = apply(adonthellc.gamedata_directory,args)
        return val
    def description(*args):
        val = apply(adonthellc.gamedata_description,args)
        return val
    def location(*args):
        val = apply(adonthellc.gamedata_location,args)
        return val
    def time(*args):
        val = apply(adonthellc.gamedata_time,args)
        return val
    def set_description(*args):
        val = apply(adonthellc.gamedata_set_description,args)
        return val
    def set_directory(*args):
        val = apply(adonthellc.gamedata_set_directory,args)
        return val
    def __repr__(self):
        return "<C gamedata instance at %s>" % (self.this,)
class gamedataPtr(gamedata):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = gamedata



class game:
    def __init__(self,*args):
        self.this = apply(adonthellc.new_game,args)
        self.thisown = 1

    def __del__(self,adonthellc=adonthellc):
        if getattr(self,'thisown',0):
            adonthellc.delete_game(self)
    def __repr__(self):
        return "<C game instance at %s>" % (self.this,)
class gamePtr(game):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = game





#-------------- FUNCTION WRAPPERS ------------------

fileops_put_version = adonthellc.fileops_put_version

fileops_get_version = adonthellc.fileops_get_version

event_list_register_event = adonthellc.event_list_register_event

event_handler_register_event = adonthellc.event_handler_register_event

event_handler_remove_event = adonthellc.event_handler_remove_event

event_handler_raise_event = adonthellc.event_handler_raise_event

gametime_start_action = adonthellc.gametime_start_action

gametime_stop_action = adonthellc.gametime_stop_action

gametime_frames_to_do = adonthellc.gametime_frames_to_do

gametime_update = adonthellc.gametime_update

input_init = adonthellc.input_init

input_shutdown = adonthellc.input_shutdown

input_update = adonthellc.input_update

input_is_pushed = adonthellc.input_is_pushed

input_has_been_pushed = adonthellc.input_has_been_pushed

input_get_next_key = adonthellc.input_get_next_key

input_get_next_unicode = adonthellc.input_get_next_unicode

input_set_key_repeat = adonthellc.input_set_key_repeat

input_clear_keys_queue = adonthellc.input_clear_keys_queue

audio_init = adonthellc.audio_init

audio_cleanup = adonthellc.audio_cleanup

audio_load_background = adonthellc.audio_load_background

audio_unload_background = adonthellc.audio_unload_background

audio_set_background_volume = adonthellc.audio_set_background_volume

audio_pause_music = adonthellc.audio_pause_music

audio_unpause_music = adonthellc.audio_unpause_music

audio_load_wave = adonthellc.audio_load_wave

audio_unload_wave = adonthellc.audio_unload_wave

audio_play_wave = adonthellc.audio_play_wave

audio_play_background = adonthellc.audio_play_background

audio_fade_in_background = adonthellc.audio_fade_in_background

audio_fade_out_background = adonthellc.audio_fade_out_background

audio_change_background = adonthellc.audio_change_background

audio_is_initialized = adonthellc.audio_is_initialized

screen_set_video_mode = adonthellc.screen_set_video_mode

screen_length = adonthellc.screen_length

screen_height = adonthellc.screen_height

screen_bytes_per_pixel = adonthellc.screen_bytes_per_pixel

screen_trans_col = adonthellc.screen_trans_col

screen_clear = adonthellc.screen_clear

screen_show = adonthellc.screen_show

screen_is_fullscreen = adonthellc.screen_is_fullscreen

screen_set_fullscreen = adonthellc.screen_set_fullscreen

screen_info = adonthellc.screen_info

screen_transition = adonthellc.screen_transition

win_select_next = adonthellc.win_select_next

win_select_previous = adonthellc.win_select_previous

win_select_set_cur_select = adonthellc.win_select_set_cur_select

win_select_back = adonthellc.win_select_back

win_select_activate = adonthellc.win_select_activate

win_select_set_activate_keyboard = adonthellc.win_select_set_activate_keyboard

win_select_is_activate_keyboard = adonthellc.win_select_is_activate_keyboard

win_select_init = adonthellc.win_select_init

win_manager_add = adonthellc.win_manager_add

win_manager_exist = adonthellc.win_manager_exist

win_manager_remove = adonthellc.win_manager_remove

win_manager_update = adonthellc.win_manager_update

win_manager_draw = adonthellc.win_manager_draw

win_manager_set_focus = adonthellc.win_manager_set_focus

win_manager_destroy = adonthellc.win_manager_destroy

gamedata_init = adonthellc.gamedata_init

gamedata_cleanup = adonthellc.gamedata_cleanup

gamedata_load = adonthellc.gamedata_load

gamedata_save = adonthellc.gamedata_save

gamedata_unload = adonthellc.gamedata_unload

def gamedata_next_save(*args, **kwargs):
    val = apply(adonthellc.gamedata_next_save,args,kwargs)
    if val: val = gamedataPtr(val)
    return val

gamedata_user_data_dir = adonthellc.gamedata_user_data_dir

gamedata_game_data_dir = adonthellc.gamedata_game_data_dir

def gamedata_get_saved_game(*args, **kwargs):
    val = apply(adonthellc.gamedata_get_saved_game,args,kwargs)
    if val: val = gamedataPtr(val)
    return val

game_init = adonthellc.game_init

game_cleanup = adonthellc.game_cleanup



#-------------- VARIABLE WRAPPERS ------------------

Python = adonthellc.Python
C = adonthellc.C
READ = adonthellc.READ
WRITE = adonthellc.WRITE
EVENTS_DIR = adonthellc.EVENTS_DIR
ENTER_EVENT = adonthellc.ENTER_EVENT
LEAVE_EVENT = adonthellc.LEAVE_EVENT
TIME_EVENT = adonthellc.TIME_EVENT
MAX_EVENT = adonthellc.MAX_EVENT
FTD_LIMIT = adonthellc.FTD_LIMIT
CYCLE_LENGTH = adonthellc.CYCLE_LENGTH
SDLK_UNKNOWN = adonthellc.SDLK_UNKNOWN
SDLK_FIRST = adonthellc.SDLK_FIRST
SDLK_BACKSPACE = adonthellc.SDLK_BACKSPACE
SDLK_TAB = adonthellc.SDLK_TAB
SDLK_CLEAR = adonthellc.SDLK_CLEAR
SDLK_RETURN = adonthellc.SDLK_RETURN
SDLK_PAUSE = adonthellc.SDLK_PAUSE
SDLK_ESCAPE = adonthellc.SDLK_ESCAPE
SDLK_SPACE = adonthellc.SDLK_SPACE
SDLK_EXCLAIM = adonthellc.SDLK_EXCLAIM
SDLK_QUOTEDBL = adonthellc.SDLK_QUOTEDBL
SDLK_HASH = adonthellc.SDLK_HASH
SDLK_DOLLAR = adonthellc.SDLK_DOLLAR
SDLK_AMPERSAND = adonthellc.SDLK_AMPERSAND
SDLK_QUOTE = adonthellc.SDLK_QUOTE
SDLK_LEFTPAREN = adonthellc.SDLK_LEFTPAREN
SDLK_RIGHTPAREN = adonthellc.SDLK_RIGHTPAREN
SDLK_ASTERISK = adonthellc.SDLK_ASTERISK
SDLK_PLUS = adonthellc.SDLK_PLUS
SDLK_COMMA = adonthellc.SDLK_COMMA
SDLK_MINUS = adonthellc.SDLK_MINUS
SDLK_PERIOD = adonthellc.SDLK_PERIOD
SDLK_SLASH = adonthellc.SDLK_SLASH
SDLK_0 = adonthellc.SDLK_0
SDLK_1 = adonthellc.SDLK_1
SDLK_2 = adonthellc.SDLK_2
SDLK_3 = adonthellc.SDLK_3
SDLK_4 = adonthellc.SDLK_4
SDLK_5 = adonthellc.SDLK_5
SDLK_6 = adonthellc.SDLK_6
SDLK_7 = adonthellc.SDLK_7
SDLK_8 = adonthellc.SDLK_8
SDLK_9 = adonthellc.SDLK_9
SDLK_COLON = adonthellc.SDLK_COLON
SDLK_SEMICOLON = adonthellc.SDLK_SEMICOLON
SDLK_LESS = adonthellc.SDLK_LESS
SDLK_EQUALS = adonthellc.SDLK_EQUALS
SDLK_GREATER = adonthellc.SDLK_GREATER
SDLK_QUESTION = adonthellc.SDLK_QUESTION
SDLK_AT = adonthellc.SDLK_AT
SDLK_LEFTBRACKET = adonthellc.SDLK_LEFTBRACKET
SDLK_BACKSLASH = adonthellc.SDLK_BACKSLASH
SDLK_RIGHTBRACKET = adonthellc.SDLK_RIGHTBRACKET
SDLK_CARET = adonthellc.SDLK_CARET
SDLK_UNDERSCORE = adonthellc.SDLK_UNDERSCORE
SDLK_BACKQUOTE = adonthellc.SDLK_BACKQUOTE
SDLK_a = adonthellc.SDLK_a
SDLK_b = adonthellc.SDLK_b
SDLK_c = adonthellc.SDLK_c
SDLK_d = adonthellc.SDLK_d
SDLK_e = adonthellc.SDLK_e
SDLK_f = adonthellc.SDLK_f
SDLK_g = adonthellc.SDLK_g
SDLK_h = adonthellc.SDLK_h
SDLK_i = adonthellc.SDLK_i
SDLK_j = adonthellc.SDLK_j
SDLK_k = adonthellc.SDLK_k
SDLK_l = adonthellc.SDLK_l
SDLK_m = adonthellc.SDLK_m
SDLK_n = adonthellc.SDLK_n
SDLK_o = adonthellc.SDLK_o
SDLK_p = adonthellc.SDLK_p
SDLK_q = adonthellc.SDLK_q
SDLK_r = adonthellc.SDLK_r
SDLK_s = adonthellc.SDLK_s
SDLK_t = adonthellc.SDLK_t
SDLK_u = adonthellc.SDLK_u
SDLK_v = adonthellc.SDLK_v
SDLK_w = adonthellc.SDLK_w
SDLK_x = adonthellc.SDLK_x
SDLK_y = adonthellc.SDLK_y
SDLK_z = adonthellc.SDLK_z
SDLK_DELETE = adonthellc.SDLK_DELETE
SDLK_WORLD_0 = adonthellc.SDLK_WORLD_0
SDLK_WORLD_1 = adonthellc.SDLK_WORLD_1
SDLK_WORLD_2 = adonthellc.SDLK_WORLD_2
SDLK_WORLD_3 = adonthellc.SDLK_WORLD_3
SDLK_WORLD_4 = adonthellc.SDLK_WORLD_4
SDLK_WORLD_5 = adonthellc.SDLK_WORLD_5
SDLK_WORLD_6 = adonthellc.SDLK_WORLD_6
SDLK_WORLD_7 = adonthellc.SDLK_WORLD_7
SDLK_WORLD_8 = adonthellc.SDLK_WORLD_8
SDLK_WORLD_9 = adonthellc.SDLK_WORLD_9
SDLK_WORLD_10 = adonthellc.SDLK_WORLD_10
SDLK_WORLD_11 = adonthellc.SDLK_WORLD_11
SDLK_WORLD_12 = adonthellc.SDLK_WORLD_12
SDLK_WORLD_13 = adonthellc.SDLK_WORLD_13
SDLK_WORLD_14 = adonthellc.SDLK_WORLD_14
SDLK_WORLD_15 = adonthellc.SDLK_WORLD_15
SDLK_WORLD_16 = adonthellc.SDLK_WORLD_16
SDLK_WORLD_17 = adonthellc.SDLK_WORLD_17
SDLK_WORLD_18 = adonthellc.SDLK_WORLD_18
SDLK_WORLD_19 = adonthellc.SDLK_WORLD_19
SDLK_WORLD_20 = adonthellc.SDLK_WORLD_20
SDLK_WORLD_21 = adonthellc.SDLK_WORLD_21
SDLK_WORLD_22 = adonthellc.SDLK_WORLD_22
SDLK_WORLD_23 = adonthellc.SDLK_WORLD_23
SDLK_WORLD_24 = adonthellc.SDLK_WORLD_24
SDLK_WORLD_25 = adonthellc.SDLK_WORLD_25
SDLK_WORLD_26 = adonthellc.SDLK_WORLD_26
SDLK_WORLD_27 = adonthellc.SDLK_WORLD_27
SDLK_WORLD_28 = adonthellc.SDLK_WORLD_28
SDLK_WORLD_29 = adonthellc.SDLK_WORLD_29
SDLK_WORLD_30 = adonthellc.SDLK_WORLD_30
SDLK_WORLD_31 = adonthellc.SDLK_WORLD_31
SDLK_WORLD_32 = adonthellc.SDLK_WORLD_32
SDLK_WORLD_33 = adonthellc.SDLK_WORLD_33
SDLK_WORLD_34 = adonthellc.SDLK_WORLD_34
SDLK_WORLD_35 = adonthellc.SDLK_WORLD_35
SDLK_WORLD_36 = adonthellc.SDLK_WORLD_36
SDLK_WORLD_37 = adonthellc.SDLK_WORLD_37
SDLK_WORLD_38 = adonthellc.SDLK_WORLD_38
SDLK_WORLD_39 = adonthellc.SDLK_WORLD_39
SDLK_WORLD_40 = adonthellc.SDLK_WORLD_40
SDLK_WORLD_41 = adonthellc.SDLK_WORLD_41
SDLK_WORLD_42 = adonthellc.SDLK_WORLD_42
SDLK_WORLD_43 = adonthellc.SDLK_WORLD_43
SDLK_WORLD_44 = adonthellc.SDLK_WORLD_44
SDLK_WORLD_45 = adonthellc.SDLK_WORLD_45
SDLK_WORLD_46 = adonthellc.SDLK_WORLD_46
SDLK_WORLD_47 = adonthellc.SDLK_WORLD_47
SDLK_WORLD_48 = adonthellc.SDLK_WORLD_48
SDLK_WORLD_49 = adonthellc.SDLK_WORLD_49
SDLK_WORLD_50 = adonthellc.SDLK_WORLD_50
SDLK_WORLD_51 = adonthellc.SDLK_WORLD_51
SDLK_WORLD_52 = adonthellc.SDLK_WORLD_52
SDLK_WORLD_53 = adonthellc.SDLK_WORLD_53
SDLK_WORLD_54 = adonthellc.SDLK_WORLD_54
SDLK_WORLD_55 = adonthellc.SDLK_WORLD_55
SDLK_WORLD_56 = adonthellc.SDLK_WORLD_56
SDLK_WORLD_57 = adonthellc.SDLK_WORLD_57
SDLK_WORLD_58 = adonthellc.SDLK_WORLD_58
SDLK_WORLD_59 = adonthellc.SDLK_WORLD_59
SDLK_WORLD_60 = adonthellc.SDLK_WORLD_60
SDLK_WORLD_61 = adonthellc.SDLK_WORLD_61
SDLK_WORLD_62 = adonthellc.SDLK_WORLD_62
SDLK_WORLD_63 = adonthellc.SDLK_WORLD_63
SDLK_WORLD_64 = adonthellc.SDLK_WORLD_64
SDLK_WORLD_65 = adonthellc.SDLK_WORLD_65
SDLK_WORLD_66 = adonthellc.SDLK_WORLD_66
SDLK_WORLD_67 = adonthellc.SDLK_WORLD_67
SDLK_WORLD_68 = adonthellc.SDLK_WORLD_68
SDLK_WORLD_69 = adonthellc.SDLK_WORLD_69
SDLK_WORLD_70 = adonthellc.SDLK_WORLD_70
SDLK_WORLD_71 = adonthellc.SDLK_WORLD_71
SDLK_WORLD_72 = adonthellc.SDLK_WORLD_72
SDLK_WORLD_73 = adonthellc.SDLK_WORLD_73
SDLK_WORLD_74 = adonthellc.SDLK_WORLD_74
SDLK_WORLD_75 = adonthellc.SDLK_WORLD_75
SDLK_WORLD_76 = adonthellc.SDLK_WORLD_76
SDLK_WORLD_77 = adonthellc.SDLK_WORLD_77
SDLK_WORLD_78 = adonthellc.SDLK_WORLD_78
SDLK_WORLD_79 = adonthellc.SDLK_WORLD_79
SDLK_WORLD_80 = adonthellc.SDLK_WORLD_80
SDLK_WORLD_81 = adonthellc.SDLK_WORLD_81
SDLK_WORLD_82 = adonthellc.SDLK_WORLD_82
SDLK_WORLD_83 = adonthellc.SDLK_WORLD_83
SDLK_WORLD_84 = adonthellc.SDLK_WORLD_84
SDLK_WORLD_85 = adonthellc.SDLK_WORLD_85
SDLK_WORLD_86 = adonthellc.SDLK_WORLD_86
SDLK_WORLD_87 = adonthellc.SDLK_WORLD_87
SDLK_WORLD_88 = adonthellc.SDLK_WORLD_88
SDLK_WORLD_89 = adonthellc.SDLK_WORLD_89
SDLK_WORLD_90 = adonthellc.SDLK_WORLD_90
SDLK_WORLD_91 = adonthellc.SDLK_WORLD_91
SDLK_WORLD_92 = adonthellc.SDLK_WORLD_92
SDLK_WORLD_93 = adonthellc.SDLK_WORLD_93
SDLK_WORLD_94 = adonthellc.SDLK_WORLD_94
SDLK_WORLD_95 = adonthellc.SDLK_WORLD_95
SDLK_KP0 = adonthellc.SDLK_KP0
SDLK_KP1 = adonthellc.SDLK_KP1
SDLK_KP2 = adonthellc.SDLK_KP2
SDLK_KP3 = adonthellc.SDLK_KP3
SDLK_KP4 = adonthellc.SDLK_KP4
SDLK_KP5 = adonthellc.SDLK_KP5
SDLK_KP6 = adonthellc.SDLK_KP6
SDLK_KP7 = adonthellc.SDLK_KP7
SDLK_KP8 = adonthellc.SDLK_KP8
SDLK_KP9 = adonthellc.SDLK_KP9
SDLK_KP_PERIOD = adonthellc.SDLK_KP_PERIOD
SDLK_KP_DIVIDE = adonthellc.SDLK_KP_DIVIDE
SDLK_KP_MULTIPLY = adonthellc.SDLK_KP_MULTIPLY
SDLK_KP_MINUS = adonthellc.SDLK_KP_MINUS
SDLK_KP_PLUS = adonthellc.SDLK_KP_PLUS
SDLK_KP_ENTER = adonthellc.SDLK_KP_ENTER
SDLK_KP_EQUALS = adonthellc.SDLK_KP_EQUALS
SDLK_UP = adonthellc.SDLK_UP
SDLK_DOWN = adonthellc.SDLK_DOWN
SDLK_RIGHT = adonthellc.SDLK_RIGHT
SDLK_LEFT = adonthellc.SDLK_LEFT
SDLK_INSERT = adonthellc.SDLK_INSERT
SDLK_HOME = adonthellc.SDLK_HOME
SDLK_END = adonthellc.SDLK_END
SDLK_PAGEUP = adonthellc.SDLK_PAGEUP
SDLK_PAGEDOWN = adonthellc.SDLK_PAGEDOWN
SDLK_F1 = adonthellc.SDLK_F1
SDLK_F2 = adonthellc.SDLK_F2
SDLK_F3 = adonthellc.SDLK_F3
SDLK_F4 = adonthellc.SDLK_F4
SDLK_F5 = adonthellc.SDLK_F5
SDLK_F6 = adonthellc.SDLK_F6
SDLK_F7 = adonthellc.SDLK_F7
SDLK_F8 = adonthellc.SDLK_F8
SDLK_F9 = adonthellc.SDLK_F9
SDLK_F10 = adonthellc.SDLK_F10
SDLK_F11 = adonthellc.SDLK_F11
SDLK_F12 = adonthellc.SDLK_F12
SDLK_F13 = adonthellc.SDLK_F13
SDLK_F14 = adonthellc.SDLK_F14
SDLK_F15 = adonthellc.SDLK_F15
SDLK_NUMLOCK = adonthellc.SDLK_NUMLOCK
SDLK_CAPSLOCK = adonthellc.SDLK_CAPSLOCK
SDLK_SCROLLOCK = adonthellc.SDLK_SCROLLOCK
SDLK_RSHIFT = adonthellc.SDLK_RSHIFT
SDLK_LSHIFT = adonthellc.SDLK_LSHIFT
SDLK_RCTRL = adonthellc.SDLK_RCTRL
SDLK_LCTRL = adonthellc.SDLK_LCTRL
SDLK_RALT = adonthellc.SDLK_RALT
SDLK_LALT = adonthellc.SDLK_LALT
SDLK_RMETA = adonthellc.SDLK_RMETA
SDLK_LMETA = adonthellc.SDLK_LMETA
SDLK_LSUPER = adonthellc.SDLK_LSUPER
SDLK_RSUPER = adonthellc.SDLK_RSUPER
SDLK_MODE = adonthellc.SDLK_MODE
SDLK_COMPOSE = adonthellc.SDLK_COMPOSE
SDLK_HELP = adonthellc.SDLK_HELP
SDLK_PRINT = adonthellc.SDLK_PRINT
SDLK_SYSREQ = adonthellc.SDLK_SYSREQ
SDLK_BREAK = adonthellc.SDLK_BREAK
SDLK_MENU = adonthellc.SDLK_MENU
SDLK_POWER = adonthellc.SDLK_POWER
SDLK_EURO = adonthellc.SDLK_EURO
SDLK_LAST = adonthellc.SDLK_LAST
KMOD_NONE = adonthellc.KMOD_NONE
KMOD_LSHIFT = adonthellc.KMOD_LSHIFT
KMOD_RSHIFT = adonthellc.KMOD_RSHIFT
KMOD_LCTRL = adonthellc.KMOD_LCTRL
KMOD_RCTRL = adonthellc.KMOD_RCTRL
KMOD_LALT = adonthellc.KMOD_LALT
KMOD_RALT = adonthellc.KMOD_RALT
KMOD_LMETA = adonthellc.KMOD_LMETA
KMOD_RMETA = adonthellc.KMOD_RMETA
KMOD_NUM = adonthellc.KMOD_NUM
KMOD_CAPS = adonthellc.KMOD_CAPS
KMOD_MODE = adonthellc.KMOD_MODE
KMOD_RESERVED = adonthellc.KMOD_RESERVED
NUM_WAVES = adonthellc.NUM_WAVES
NUM_MUSIC = adonthellc.NUM_MUSIC
NUM_CHANNELS = adonthellc.NUM_CHANNELS
DIALOG_DIR = adonthellc.DIALOG_DIR
DWARF = adonthellc.DWARF
ELF = adonthellc.ELF
HALFELF = adonthellc.HALFELF
HUMAN = adonthellc.HUMAN
FEMALE = adonthellc.FEMALE
MALE = adonthellc.MALE
PLAY = adonthellc.PLAY
STOP = adonthellc.STOP
MAPSQUARE_SIZE = adonthellc.MAPSQUARE_SIZE
ALL_WALKABLE = adonthellc.ALL_WALKABLE
WALKABLE_SOUTH = adonthellc.WALKABLE_SOUTH
WALKABLE_NORTH = adonthellc.WALKABLE_NORTH
WALKABLE_EAST = adonthellc.WALKABLE_EAST
WALKABLE_WEST = adonthellc.WALKABLE_WEST
NONE_WALKABLE = adonthellc.NONE_WALKABLE
MAPOBJECTS_DIR = adonthellc.MAPOBJECTS_DIR
MAPCHAR_DIR = adonthellc.MAPCHAR_DIR
STAND_NORTH = adonthellc.STAND_NORTH
STAND_SOUTH = adonthellc.STAND_SOUTH
STAND_WEST = adonthellc.STAND_WEST
STAND_EAST = adonthellc.STAND_EAST
WALK_NORTH = adonthellc.WALK_NORTH
WALK_SOUTH = adonthellc.WALK_SOUTH
WALK_WEST = adonthellc.WALK_WEST
WALK_EAST = adonthellc.WALK_EAST
NBR_MOVES = adonthellc.NBR_MOVES
NO_MOVE = adonthellc.NO_MOVE
MAPS_DIR = adonthellc.MAPS_DIR
WIN_NB_TABLE_CHAR = adonthellc.WIN_NB_TABLE_CHAR
WIN_TEXT_MAX_LENGTH = adonthellc.WIN_TEXT_MAX_LENGTH
WIN_FONT_HEIGHT = adonthellc.WIN_FONT_HEIGHT
WIN_FONT_LENGHT = adonthellc.WIN_FONT_LENGHT
WIN_SPACE_LENGHT = adonthellc.WIN_SPACE_LENGHT
WIN_ALIGN_LEFT = adonthellc.WIN_ALIGN_LEFT
WIN_ALIGN_RIGHT = adonthellc.WIN_ALIGN_RIGHT
WIN_ALIGN_CENTER = adonthellc.WIN_ALIGN_CENTER
WIN_ALIGN_NONE = adonthellc.WIN_ALIGN_NONE
WIN_LAYOUT_NO = adonthellc.WIN_LAYOUT_NO
WIN_LAYOUT_LIST = adonthellc.WIN_LAYOUT_LIST
WIN_LAYOUT_AUTO = adonthellc.WIN_LAYOUT_AUTO
WIN_DIRECTORY = adonthellc.WIN_DIRECTORY
WIN_FONT_DIRECTORY = adonthellc.WIN_FONT_DIRECTORY
WIN_BORDER_DIRECTORY = adonthellc.WIN_BORDER_DIRECTORY
WIN_BACKGROUND_DIRECTORY = adonthellc.WIN_BACKGROUND_DIRECTORY
WIN_SCROLLBAR_DIRECTORY = adonthellc.WIN_SCROLLBAR_DIRECTORY
WIN_CURSOR_DIRECTORY = adonthellc.WIN_CURSOR_DIRECTORY
WIN_FONT_FILE_IDX = adonthellc.WIN_FONT_FILE_IDX
WIN_FONT_FILE_PIC = adonthellc.WIN_FONT_FILE_PIC
WIN_FONT_FILE = adonthellc.WIN_FONT_FILE
WIN_CURSOR_BLINKING = adonthellc.WIN_CURSOR_BLINKING
WIN_V_BORDER_TEMPLATE_FILE = adonthellc.WIN_V_BORDER_TEMPLATE_FILE
WIN_H_BORDER_TEMPLATE_FILE = adonthellc.WIN_H_BORDER_TEMPLATE_FILE
WIN_CORNER_TOP_LEFT_FILE = adonthellc.WIN_CORNER_TOP_LEFT_FILE
WIN_CORNER_TOP_RIGHT_FILE = adonthellc.WIN_CORNER_TOP_RIGHT_FILE
WIN_CORNER_BOTTOM_LEFT_FILE = adonthellc.WIN_CORNER_BOTTOM_LEFT_FILE
WIN_CORNER_BOTTOM_RIGHT_FILE = adonthellc.WIN_CORNER_BOTTOM_RIGHT_FILE
WIN_BACKGROUND_FILE = adonthellc.WIN_BACKGROUND_FILE
WIN_SCROLLBAR_BAR_TOP = adonthellc.WIN_SCROLLBAR_BAR_TOP
WIN_SCROLLBAR_BAR_MID = adonthellc.WIN_SCROLLBAR_BAR_MID
WIN_SCROLLBAR_BAR_BOT = adonthellc.WIN_SCROLLBAR_BAR_BOT
WIN_SCROLLBAR_BAR_FLEX = adonthellc.WIN_SCROLLBAR_BAR_FLEX
WIN_SCROLLBAR_BACK_TOP = adonthellc.WIN_SCROLLBAR_BACK_TOP
WIN_SCROLLBAR_BACK_MID = adonthellc.WIN_SCROLLBAR_BACK_MID
WIN_SCROLLBAR_BACK_BOT = adonthellc.WIN_SCROLLBAR_BACK_BOT
WIN_CURSOR_FILE = adonthellc.WIN_CURSOR_FILE
WIN_BORDER_NORMAL_SIZE = adonthellc.WIN_BORDER_NORMAL_SIZE
WIN_BORDER_MINI_SIZE = adonthellc.WIN_BORDER_MINI_SIZE
WIN_THEME_ORIGINAL = adonthellc.WIN_THEME_ORIGINAL
WIN_THEME_ELFE = adonthellc.WIN_THEME_ELFE
WIN_OBJ_BASE = adonthellc.WIN_OBJ_BASE
WIN_OBJ_LABEL = adonthellc.WIN_OBJ_LABEL
WIN_OBJ_WRITE = adonthellc.WIN_OBJ_WRITE
WIN_OBJ_IMAGE = adonthellc.WIN_OBJ_IMAGE
WIN_OBJ_CONTAINER = adonthellc.WIN_OBJ_CONTAINER
WIN_OBJ_SCROLLED = adonthellc.WIN_OBJ_SCROLLED
WIN_OBJ_SELECT = adonthellc.WIN_OBJ_SELECT
WIN_SIG_ACTIVATE = adonthellc.WIN_SIG_ACTIVATE
WIN_SIG_UNACTIVATE = adonthellc.WIN_SIG_UNACTIVATE
WIN_SIG_UPDATE = adonthellc.WIN_SIG_UPDATE
WIN_SIG_DRAW = adonthellc.WIN_SIG_DRAW
WIN_SIG_DRAW_ONLY_VISIBLE = adonthellc.WIN_SIG_DRAW_ONLY_VISIBLE
WIN_SIG_ACTIVATE_KEY = adonthellc.WIN_SIG_ACTIVATE_KEY
WIN_SIG_NEXT_KEY = adonthellc.WIN_SIG_NEXT_KEY
WIN_SIG_PREVIOUS_KEY = adonthellc.WIN_SIG_PREVIOUS_KEY
WIN_SIG_SCROLL_UP = adonthellc.WIN_SIG_SCROLL_UP
WIN_SIG_SCROLL_DOWN = adonthellc.WIN_SIG_SCROLL_DOWN
WIN_SIG_SELECT = adonthellc.WIN_SIG_SELECT
WIN_SIG_UNSELECT = adonthellc.WIN_SIG_UNSELECT
WIN_SIG_KEYBOARD = adonthellc.WIN_SIG_KEYBOARD
WIN_SIG_DESTROY = adonthellc.WIN_SIG_DESTROY
WIN_SIG_CLOSE = adonthellc.WIN_SIG_CLOSE
WIN_SELECT_MODE_BRIGHTNESS = adonthellc.WIN_SELECT_MODE_BRIGHTNESS
WIN_SELECT_MODE_BORDER = adonthellc.WIN_SELECT_MODE_BORDER
WIN_SELECT_MODE_CURSOR = adonthellc.WIN_SELECT_MODE_CURSOR
WIN_SIZE_NORMAL = adonthellc.WIN_SIZE_NORMAL
WIN_SIZE_MINI = adonthellc.WIN_SIZE_MINI
WIN_SELECT_TYPE_NORMAL = adonthellc.WIN_SELECT_TYPE_NORMAL
WIN_SELECT_TYPE_SCROLL = adonthellc.WIN_SELECT_TYPE_SCROLL
WIN_SCROLLBAR_PAD_DEFAULT = adonthellc.WIN_SCROLLBAR_PAD_DEFAULT
WIN_SPACE_BETWEEN_BORDER = adonthellc.WIN_SPACE_BETWEEN_BORDER
WIN_SPACE_BETWEEN_OBJECT = adonthellc.WIN_SPACE_BETWEEN_OBJECT
MAX_COLOR = adonthellc.MAX_COLOR
LOAD_SCREEN = adonthellc.LOAD_SCREEN
SAVE_SCREEN = adonthellc.SAVE_SCREEN
INIT_NONE = adonthellc.INIT_NONE
INIT_VIDEO = adonthellc.INIT_VIDEO
INIT_AUDIO = adonthellc.INIT_AUDIO
INIT_PYTHON = adonthellc.INIT_PYTHON
INIT_DATA = adonthellc.INIT_DATA
INIT_SAVES = adonthellc.INIT_SAVES
INIT_INPUT = adonthellc.INIT_INPUT
INIT_ALL = adonthellc.INIT_ALL
cvar = adonthellc.cvar
screen_display = surfacePtr(adonthellc.cvar.screen_display)
