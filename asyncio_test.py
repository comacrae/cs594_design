from mistyPy.Events import Events
from utils import get_robot

misty = get_robot()

def bumped(data):
    misty.speak("I got bumped")

misty.register_event(event_name='bump_event', event_type=Events.BumpSensor, callback_function=bumped, keep_alive=True)

misty.keep_alive()