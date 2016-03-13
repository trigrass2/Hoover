#!/usr/bin/python3

import time
from robot.track import RobotEngine
from robot.sonar.asdic import ASDIC
from robot.motors.motor_servo import PWM

robot = RobotEngine()
asdic = ASDIC()

MAX_SPEED = 40


while 1:
    distance = asdic.ping()
    print(distance)
    if distance < 10:
        robot.speed_motor(-MAX_SPEED)
    if distance < 20:
        robot.stop()
    if distance < 40:
        robot.turn(30)
    else:
        robot.speed_motor(MAX_SPEED)
    time.sleep(0.01)
