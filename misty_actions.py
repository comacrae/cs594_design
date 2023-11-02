import random
from mistyPy.Events import Events
import threading
from utils import *


def change_led(self,action):
    cfg = load_cfg()
    self.misty.change_led(*['led'][action])

def pet(event):
    #misty.move_arm(arm='right', position=, velocity=50)
    return


def random_cute_noise(self):
    noise_files = load_cute_noises()
    idx = random.randint(0,len(noise_files)-1)
    self.misty.play_audio(noise_files[idx])

def throw_animation(self):
    self.misty.change_led("throw")
    self.misty.set_blinking(True)
    self.misty.move_arm(arm='left', position=29, velocity=50, duration=1.5)
    threading.Timer(2, throw_start).start()
def throw_start(self):
    self.misty.speak("throwing")
    self.misty.move_arm(arm='left', position=-60, velocity=100)
    self.misty.change_led("default")
    self.misty.set_blinking(False)

def register_misty_events(self):
    return
