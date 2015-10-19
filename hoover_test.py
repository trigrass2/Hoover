#!/usr/bin/python3
from robot.track import RobotEngine

import time

re = RobotEngine()
re.forward()
re.speed(50)
time.sleep(2)
re.left()
time.sleep(2)
re.right()
time.sleep(2)

