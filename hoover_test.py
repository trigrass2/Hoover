#!/usr/bin/python3
from robot.track import RobotEngine

import time

re = RobotEngine()
re.speed(-30)
time.sleep(2)
re.speed(30)
time.sleep(2)
re.speed(30)
re.turn(15)
time.sleep(2)
re.speed(30)
re.turn(-15)
time.sleep(2)
re.speed(50)
re.turn(50, inplace=True)
time.sleep(2)
re.turn(-50, inplace=True)
time.sleep(2)

