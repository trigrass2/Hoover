#!/usr/bin/python3
from robot.track import RobotEngine

import time

re = RobotEngine()

re.speed(30)
time.sleep(3)
re.turn(20)
time.sleep(3)
re.speed(30)
re.turn(-20)
time.sleep(3)
