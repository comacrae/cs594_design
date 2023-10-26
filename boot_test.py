import asyncio,json
from utils import *
misty = get_robot()

cfg = json.load(open('./config.json'))
if __name__ == "__main__":
    misty.display_text("connected")
