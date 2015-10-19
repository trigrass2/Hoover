#!/usr/bin/python3
from robot.motors.motor import Motor, DCMotor

import time
import atexit

def stop_motors():
	motor = Motor(addr=0x60)
	motor.getMotor(1).run(Motor.RELEASE)
	motor.getMotor(2).run(Motor.RELEASE)
	motor.getMotor(3).run(Motor.RELEASE)
	motor.getMotor(4).run(Motor.RELEASE)

atexit.register(stop_motors)


class RobotEngine:
	
	MAX_SPEED = 100
	
	def __init__(self):
		self.current_speed = 0
		
		# create a default object, no changes to I2C address or frequency
		self.motor = Motor(addr=0x60)
		
		# init motors
		self.left_motor = self.motor.getMotor(2)
		self.right_motor = self.motor.getMotor(3)
		
		# set the speed to start, from 0 (off) to 255 (max speed)
		self.left_motor.setSpeed(100)
		self.left_motor.run(Motor.FORWARD);
		self.right_motor.setSpeed(100)
		self.right_motor.run(Motor.FORWARD);
		
		# turn on motor
		self.left_motor.run(Motor.RELEASE);
		self.right_motor.run(Motor.RELEASE);
		
		self.left_motor.setSpeed(0)
		self.right_motor.setSpeed(0)


	def speed(self, value_speed):
		if value_speed < 0:
			value_speed = 0
		elif value_speed > RobotEngine.MAX_SPEED:
			value_speed = RobotEngine.MAX_SPEED
		self.current_speed = value_speed
		
		self.left_motor.setSpeed(self.current_speed)
		self.right_motor.setSpeed(self.current_speed)
			


	def forward(self):
		self.left_motor.run(Motor.FORWARD)
		self.right_motor.run(Motor.FORWARD)


	def backward(self):
		self.left_motor.run(Motor.BACKWARD)
		self.right_motor.run(Motor.BACKWARD)
	    
	    
	def left(self, angle, intime= 0, inplace = False):
		self.left_motor.run(Motor.BACKWARD)
		self.right_motor.run(Motor.FORWARD)


	def right(self, angle, intime = 0, inplace = False):
		if inplace:
			self.speed(0)
		self.left_motor.run(Motor.FORWARD)
		self.right_motor.run(Motor.BACKWARD)


	def stop(self):
		self.speed(0)


	def off(self):
		self.left_motor.run(Motor.RELEASE)
		self.right_motor.run(Motor.RELEASE)
		self.motor.getMotor(1).run(Motor.RELEASE)
		self.motor.getMotor(2).run(Motor.RELEASE)
		self.motor.getMotor(3).run(Motor.RELEASE)
		self.motor.getMotor(4).run(Motor.RELEASE)



