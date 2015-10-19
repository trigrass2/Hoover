#!/usr/bin/python3
from hoover.motors.motor import Motor, DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Motor(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Motor.RELEASE)
	mh.getMotor(2).run(Motor.RELEASE)
	mh.getMotor(3).run(Motor.RELEASE)
	mh.getMotor(4).run(Motor.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
lMotor = mh.getMotor(2)
rMotor = mh.getMotor(3)

# set the speed to start, from 0 (off) to 255 (max speed)
lMotor.setSpeed(100)
lMotor.run(Motor.FORWARD);
rMotor.setSpeed(100)
rMotor.run(Motor.FORWARD);

# turn on motor
lMotor.run(Motor.RELEASE);
rMotor.run(Motor.RELEASE);


while (True):
	print("Forward!")
	lMotor.run(Motor.FORWARD)
	rMotor.run(Motor.FORWARD)

	print("\tSpeed up...")
	for i in range(100):
		lMotor.setSpeed(i)
		rMotor.setSpeed(i)
		time.sleep(0.1)

	print("\tSlow down...")
	for i in reversed(range(100)):
		lMotor.setSpeed(i)
		rMotor.setSpeed(i)
		time.sleep(0.1)

	print("Backward!")
	lMotor.run(Motor.BACKWARD)
	rMotor.run(Motor.BACKWARD)

	print("\tSpeed up...")
	for i in range(100):
		lMotor.setSpeed(i)
		rMotor.setSpeed(i)
		time.sleep(0.1)

	print("\tSlow down...")
	for i in reversed(range(100)):
		lMotor.setSpeed(i)
		rMotor.setSpeed(i)
		time.sleep(0.1)

	print("Release")
	lMotor.run(Motor.RELEASE)
	rMotor.run(Motor.RELEASE)
	time.sleep(1.0)
