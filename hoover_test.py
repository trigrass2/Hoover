#!/usr/bin/python3
from robot.track import RobotEngine

import time

re = RobotEngine()

re.turn(20)
time.sleep(3)
re.speed_motor(20)
time.sleep(3)
re.stop()
time.sleep(1)
re.speed_motor(30)
time.sleep(3)
re.stop()



