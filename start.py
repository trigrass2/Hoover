#!/usr/bin/python3

import time
from robot.track import RobotEngine
from robot.sonar.asdic import ASDIC
from robot.motors.motor_servo import PWM

MAX_SPEED = 40

class Servo:
    FREQ = 50
    def __init__(self):
        self.pwm = PWM(0x60, debug=False)

    def left(self):
        self.pwm.setPWMFreq(Servo.FREQ)
        self.pwm.setPWM(14, 0, 450)
        time.sleep(0.5)
        self.pwm.setPWM(14, 0, 0)
        self.pwm.setPWMFreq(1000)

    def right(self):
        self.pwm.setPWMFreq(Servo.FREQ)
        self.pwm.setPWM(14, 0, 110)
        time.sleep(0.5)
        self.pwm.setPWM(14, 0, 0)
        self.pwm.setPWMFreq(1000)

    def zero(self):
        self.pwm.setPWMFreq(Servo.FREQ)
        self.pwm.setPWM(14, 0, 250)
        time.sleep(0.5)
        self.pwm.setPWM(14, 0, 0)
        self.pwm.setPWMFreq(1000)

    def restore_freq(self):
        self.pwm.setPWMFreq(1000)


robot = RobotEngine()
asdic = ASDIC()
servo = Servo()

def direction():
    servo.left()
    distance_left = asdic.ping()
    servo.right()
    distance_right = asdic.ping()
    servo.zero()
    if distance_left > distance_right:
        return -1
    return 1


while 1:
    distance = asdic.distance()
    print(distance)

    if distance < 10:
        robot.speed_motor(-MAX_SPEED)
    elif distance < 20:
        robot.stop()
        robot.turn(20 * direction())
        time.sleep(0.5)
    elif distance < 40:
        robot.turn(30 * direction())
    else:
        robot.speed_motor(MAX_SPEED)
    time.sleep(0.01)
