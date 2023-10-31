from mistyPy.Events import Events
from utils import get_robot
import threading
import keyboard
import random

misty = get_robot()
#misty.start_object_detector(minimumConfidence=0.5,modelId=0,maxTrackerHistory=5)
misty.speak('listening')

def get_audio():
    with open('audio_files.txt', 'w+') as f:
        l = misty.get_audio_list().json()['result']
        for item in l:
            if item['systemAsset']:
                f.write(f"{item['name']}\n")
        f.close()
    return

def random_cute_noise():
    noise_files = [
    's_Awe.wav',
    's_Awe2.wav',
    's_Awe3.wav'
        ]
    idx = random.randint(0,len(noise_files)-1)
    misty.play_audio(noise_files[idx])

def throw_animation():
    misty.move_arm(arm='left', position=29, velocity=50, duration=1.5)
    threading.Timer(2, throw_start).start()

valid_keys = ['a','w','s','d','1','2','q']
keys_down = {k : False for k in valid_keys}


def press_key(e, k,func, *args):
    if not keys_down[k]:
        print('pressed', k)
        print(f'calling {str(func)}{args}')
        keys_down[k] = True
        func(*args)
def release_key(e,k,func, *args):
    print('released', k)
    print(f'calling {str(func)}{args}')
    keys_down[k] = False
    if func is not None:
        func(*args)


keyboard.on_press_key('w', lambda e: press_key(e,'w',misty.drive,100,0), True)
keyboard.on_release_key('w',lambda e: release_key(e,'w', misty.stop), True)
keyboard.on_press_key('s', lambda e: press_key(e,'s',misty.drive,-100,0), True)
keyboard.on_release_key('s',lambda e: release_key(e,'s', misty.stop), True)
keyboard.on_press_key('d', lambda e: press_key(e,'d',misty.drive,0,-100), True)
keyboard.on_release_key('d',lambda e: release_key(e,'d', misty.stop), True)
keyboard.on_press_key('a', lambda e: press_key(e,'a',misty.drive,0,100), True)
keyboard.on_release_key('a',lambda e: release_key(e,'a', misty.stop), True)
keyboard.on_press_key('1', lambda e: press_key(e,'1',misty.speak,'good boy'), True)
keyboard.on_release_key('1',lambda e: release_key(e,'1',None), True)
keyboard.on_press_key('2', lambda e: press_key(e,'2',misty.speak,'come here buddy!'), True)
keyboard.on_release_key('2',lambda e: release_key(e,'2', misty.stop), True)
keyboard.on_press_key('q', lambda e: press_key(e,'q',random_cute_noise), True)
keyboard.on_release_key('q',lambda e: release_key(e,'q', None), True)



def goodboy(event):
    msg = event['message']
    if(msg['description'] in ['dog','cat']):
        misty.speak("good boy")
        misty.unregister_event('goodboy_event')
    return
def nuzzle(event):
    msg = event['message']
def throw_setup(event):
    msg = event['message']
    contacted = msg['isContacted']
    print(f"CONTACTED:{contacted}")
    sensor = msg['sensorId']
    print(f"SENSOR:{sensor}")
    if contacted==True and sensor == 'bfr':
        throw_animation()
    return

def throw_start():
    misty.speak("throwing")
    misty.move_arm(arm='left', position=-60, velocity=100)

#misty.register_event(event_name='goodboy_event', event_type=Events.ObjectDetection, callback_function=goodboy, keep_alive=True)
misty.register_event(event_name='throw_event', event_type=Events.BumpSensor, callback_function=throw_setup, keep_alive=True)


misty.keep_alive()