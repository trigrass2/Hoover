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
		self.left_speed = 0
		self.right_speed = 0
		self.current_speed = 0
		
		# create a default object, no changes to I2C address or frequency
		self.motor = Motor(addr=0x60)
		
		# init motors
		self.left_motor = self.motor.getMotor(2)
		self.right_motor = self.motor.getMotor(3)

		self.left_motor.run(Motor.FORWARD);
		self.right_motor.run(Motor.FORWARD);
		
		# turn on motor
		self.left_motor.run(Motor.RELEASE);
		self.right_motor.run(Motor.RELEASE);


	def speed_motor_left(self, to_speed):
		if to_speed > 0:
			self.left_motor.run(Motor.FORWARD)
		else:
			self.left_motor.run(Motor.BACKWARD)
		
		if to_speed > RobotEngine.MAX_SPEED:
			to_speed = RobotEngine.MAX_SPEED
		elif to_speed < -RobotEngine.MAX_SPEED:
			to_speed = RobotEngine.MAX_SPEED

		self.left_speed = abs(to_speed)
		self.left_motor.setSpeed(self.left_speed)
		return self.left_speed
		
		
	def speed_motor_right(self, to_speed):
		if to_speed > 0:
			self.right_motor.run(Motor.FORWARD)
		else:
			self.right_motor.run(Motor.BACKWARD)
		
		if to_speed > RobotEngine.MAX_SPEED:
			to_speed = RobotEngine.MAX_SPEED
		elif to_speed < -RobotEngine.MAX_SPEED:
			to_speed = RobotEngine.MAX_SPEED

		self.right_speed = abs(to_speed)
		self.right_motor.setSpeed(self.right_speed)
		return self.right_speed


	def speed(self, value_speed):
		current_speed = self.speed_motor_left(value_speed)
		self.speed_motor_right(value_speed)
		self.current_speed = current_speed


	def turn(self, speed_turn, inplace = False):
		if inplace:
			if speed_turn > 0:
				self.left_motor.run(Motor.BACKWARD)
				self.right_motor.run(Motor.FORWARD)
			if speed_turn < 0:
				self.left_motor.run(Motor.FORWARD)
				self.right_motor.run(Motor.BACKWARD)
		else:
			if speed_turn > 0:
				self.speed_motor_right(self.right_speed - abs(speed_turn))
			if speed_turn < 0:
				self.speed_motor_left(self.left_speed - abs(speed_turn))


	def stop(self):
		self.speed(0)


	def off(self):
		self.left_motor.run(Motor.RELEASE)
		self.right_motor.run(Motor.RELEASE)
		self.motor.getMotor(1).run(Motor.RELEASE)
		self.motor.getMotor(2).run(Motor.RELEASE)
		self.motor.getMotor(3).run(Motor.RELEASE)
		self.motor.getMotor(4).run(Motor.RELEASE)



