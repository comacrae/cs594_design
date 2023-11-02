import json
from mistyPy.GenerateRobot import RobotGenerator
from mistyPy.Robot import Robot


def load_cfg(config_path='./config.json'):
    return json.load(open('./config.json'))
def get_keys_down_dict():
    cfg = load_cfg()
    return {k : False for k in cfg['valid_keys']}

def get_robot():
    cfg = load_cfg()
    RobotGenerator(ip=cfg['ip'])
    misty = Robot(cfg['ip'])
    misty.keep_alive()
    return misty

def get_audio_files():
    with open('audio_files.txt', 'w+') as f:
        l = get_robot().get_audio_list().json()['result']
        for item in l:
            if item['systemAsset']:
                f.write(f"{item['name']}\n")
        f.close()
    return

def load_cute_noises():
    return load_cfg()['audio']['cute']
def load_phrases():
    return load_cfg()['audio']['phrases']