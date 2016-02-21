#!/usr/bin/python3
import sys
from robot.track import RobotEngine

import time
from robot.motors.motor_servo import PWM

FREQ = 50
#FREQ = 1000 on = 1 off = 500 servo kreci sie caly czas do przodu.
"""
FREQ = 50
pi@raspberrypi ~/projects/Hoover $ ./hoover_test.py 0 450 lewo
pi@raspberrypi ~/projects/Hoover $ ./hoover_test.py 0 108 prawo
pi@raspberrypi ~/projects/Hoover $ ./hoover_test.py 0 250 zero
"""

class Servo:
    FREQ = 50
    def __init__(self):
        self.pwm = PWM(0x60, debug=False)
        self.pwm.setPWMFreq(Servo.FREQ)

    def left(self):
        self.pwm.setPWM(14, 0, 450)
        time.sleep(0.5)
        self.pwm.setPWM(14, 0, 0)

    def right(self):
        self.pwm.setPWM(14, 0, 110)
        time.sleep(0.5)
        self.pwm.setPWM(14, 0, 0)

    def zero(self):
        self.pwm.setPWM(14, 0, 250)
        time.sleep(0.5)
        self.pwm.setPWM(14, 0, 0)

 

def pulse(servo_pulse):
	pulse_length = 1000000 / FREQ / 4096
	servo_pulse *= 1000
	servo_pulse /= pulse_length
	print(servo_pulse)
	return int(servo_pulse)




servo = Servo()
if sys.argv[1] == 'l':
    servo.left()
elif sys.argv[1] == 'r':
    servo.right()
elif sys.argv[1] == 'z':
    servo.zero()
#time.sleep(2)
#servo.zero()
#time.sleep(2)

"""
f1 = int(sys.argv[1])
f2 = int(sys.argv[2])
pwm = PWM(0x60, debug=False)
pwm.setPWMFreq(FREQ)

pwm.setPWM(14, f1, f2)
time.sleep(4)

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
