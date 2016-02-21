#!/usr/bin/python3
from robot.track import RobotEngine

import time
from robot.motors.motor_servo import PWM

pwm = PWM(0x60, debug=True)
pwm.setPWMFreq(100)
pwm.setPWM(14, 0, 100)
time.sleep(2)
pwm.setPWM(14, 25, 1000)
time.sleep(2)

"""
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
"""


