import json
from mistyPy.GenerateRobot import RobotGenerator
from mistyPy.Robot import Robot

def get_robot(cfg_path='./config.json'):
    cfg = json.load(open('./config.json'))
    RobotGenerator(ip=cfg['ip'])
    misty = Robot(cfg['ip'])
    return misty
