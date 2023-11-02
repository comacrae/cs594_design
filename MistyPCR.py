import random
from mistyPy.Events import Events
import threading
from utils import *
from keyboard_events import press_key,release_key
import keyboard

class MistyPCR():
    def __init__(self,misty):
        self.misty=misty
        self.register_driving()
        self.register_speaking()
        self.register_actions()
        self.register_misty_events()
        self.state='default'

    def register_driving(self):
        keyboard.on_press_key('w', lambda e: press_key(e, 'w', self.misty.drive, 100, 0), True)
        keyboard.on_release_key('w', lambda e: release_key(e, 'w', self.misty.stop), True)
        keyboard.on_press_key('s', lambda e: press_key(e, 's', self.misty.drive, -100, 0), True)
        keyboard.on_release_key('s', lambda e: release_key(e, 's', self.misty.stop), True)
        keyboard.on_press_key('d', lambda e: press_key(e, 'd', self.misty.drive, 0, -100), True)
        keyboard.on_release_key('d', lambda e: release_key(e, 'd', self.misty.stop), True)
        keyboard.on_press_key('a', lambda e: press_key(e, 'a', self.misty.drive, 0, 100), True)
        keyboard.on_release_key('a', lambda e: release_key(e, 'a', self.misty.stop), True)

    def register_speaking(self):
        keyboard.on_press_key('1', lambda e: press_key(e, '1', self.speak, "admiration", "greeting"), True)
        keyboard.on_release_key('1', lambda e: release_key(e, '1', None), True)
        keyboard.on_press_key('2', lambda e: press_key(e, '2', self.speak, "admiration", "good_boy"), True)
        keyboard.on_release_key('2', lambda e: release_key(e, '2', None), True)
        keyboard.on_press_key('i', lambda e: press_key(e, 'i', self.speak, None, "introduction"),
                              True)  # dog is a mediator
        keyboard.on_release_key('i', lambda e: release_key(e, 'i', None), True)
        keyboard.on_press_key('q', lambda e: press_key(e, 'q', self.random_cute_noise), True)
        keyboard.on_release_key('q', lambda e: release_key(e, 'q', None), True)
        return

    def register_actions(self):
        keyboard.on_press_key('r', lambda e: press_key(e, 'r', self.throw_start), True)
        keyboard.on_release_key('r', lambda e: release_key(e, 'r', None), True)
        keyboard.on_press_key('p', lambda e: press_key(e, 'p', self.pet_up), True)
        keyboard.on_release_key('p', lambda e: release_key(e, 'p', self.pet_down), True)
        return

    def speak(self,face, phrase):
        phrases = load_phrases()
        if face is not None:
            self.change_face(face)
        self.misty.speak(phrases[phrase])
        self.change_face("default")
    def change_face(self, face):
        if face == "default":
            self.misty.display_image("e_DefaultContent.jpg")
        elif face=="admiration":
            self.misty.display_image("e_Admiration.jpg")
        return

    def change_led(self, action):
        cfg = load_cfg()
        self.misty.change_led(*cfg['led'][action])

    def pet_up(self):
        if self.state != 'pet':
            self.state='pet'
            threading.Timer(5, self.end_pet)
        self.change_led("pet")
        self.misty.move_arm(arm='right', position=-35, velocity=50)
        return
    def pet_down(self):
        self.misty.move_arm(arm='right', position=0, velocity=50)
        return

    def end_pet(self):
        self.change_led("default")
        self.state="default"
        return

    def random_cute_noise(self):
        noise_files = load_cute_noises()
        idx = random.randint(0, len(noise_files) - 1)
        self.misty.play_audio(noise_files[idx])

    def throw_animation(self):
        self.misty.move_arm(arm='left', position=0, velocity=100)
        self.change_led("default")
        self.misty.set_blinking(False)

    def throw_start(self):
        self.change_led("throw")
        self.misty.set_blinking(True)
        self.misty.speak("throwing")
        threading.Timer(3, self.throw_animation).start()
        self.misty.move_arm(arm='left', position=90, velocity=50)

    def pet_start(self):
        self.change_led("pet")


    def register_misty_events(self):
        return

    def get_misty(self):
        return self.misty

