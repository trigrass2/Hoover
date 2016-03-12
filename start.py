#!/usr/bin/python3

import time
from robot.track import RobotEngine
from robot.sonar.asdic import ASDIC
from robot.motors.motor_servo import PWM

robot = RobotEngine()
asdic = ASDIC()

robot.speed_motor(30)

while 1:
    distance = asdic.ping()
    print(distance)
    if distance < 30:
        robot.left(30)
    else:
        robot.speed_motor(30)
    time.sleep(0.01)
