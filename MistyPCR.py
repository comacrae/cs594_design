from utils import *
from keyboard_events import register_driving, register_speaking, register_actions
from misty_actions import register_misty_events

class MistyPCR():
    def __init__(self,misty):
        self.misty=misty
        register_driving(self)
        register_speaking(self)
        register_actions(self)
        register_misty_events(self)

    def get_misty(self):
        return self.misty

