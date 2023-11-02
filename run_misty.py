from MistyPCR import MistyPCR
from utils import get_robot
misty = get_robot()
m = MistyPCR(misty)

while True:
    misty.keep_alive()
