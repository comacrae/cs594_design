import keyboard
from misty_actions import *

keys_down = get_keys_down_dict() # keeps track of valid keys and which ones are pressed

def press_key(e, k,func, *args):
    if not keys_down[k]:
        keys_down[k] = True
        func(*args)
def release_key(e,k,func, *args):
    keys_down[k] = False
    if func is not None:
        func(*args)

def register_driving(self):
    keyboard.on_press_key('w', lambda e: press_key(e,'w',self.misty.drive,100,0), True)
    keyboard.on_release_key('w',lambda e: release_key(e,'w', self.misty.stop), True)
    keyboard.on_press_key('s', lambda e: press_key(e,'s',self.misty.drive,-100,0), True)
    keyboard.on_release_key('s',lambda e: release_key(e,'s', self.misty.stop), True)
    keyboard.on_press_key('d', lambda e: press_key(e,'d',self.misty.drive,0,-100), True)
    keyboard.on_release_key('d',lambda e: release_key(e,'d', self.misty.stop), True)
    keyboard.on_press_key('a', lambda e: press_key(e,'a',self.misty.drive,0,100), True)
    keyboard.on_release_key('a',lambda e: release_key(e,'a', self.misty.stop), True)
def register_speaking(self):
    phrases = load_phrases()
    keyboard.on_press_key('1', lambda e: press_key(e,'1',self.misty.speak,phrases['greeting']), True)
    keyboard.on_release_key('1',lambda e: release_key(e,'1',None), True)
    keyboard.on_press_key('2', lambda e: press_key(e,'2',self.misty.speak,phrases['good_boy']), True)
    keyboard.on_release_key('2',lambda e: release_key(e,'2', None), True)
    keyboard.on_press_key('i', lambda e: press_key(e,'i',self.misty.speak,phrases['introduction']), True) # dog is a mediator
    keyboard.on_release_key('i',lambda e: release_key(e,'i',None), True)
    keyboard.on_press_key('q', lambda e: press_key(e,'q',random_cute_noise,self), True)
    keyboard.on_release_key('q',lambda e: release_key(e,'q', None), True)
    return

def register_actions(self):
    keyboard.on_press_key('r', lambda e: press_key(e, 'r', throw_start,self), True)
    keyboard.on_release_key('r', lambda e: release_key(e, 'r', None), True)
    return

