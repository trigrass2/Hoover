#!/usr/bin/python3
# Anti-Submarine Division

import RPi.GPIO as GPIO
import time, atexit

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)


class ASDIC:
    def __init__(self):
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)

        GPIO.output(TRIG, False)
        print("Waiting for sensor to settle...")
        time.sleep(1)
        print("[DONE]")

    def clean(self):
        GPIO.cleanup()

    def ping(self):
        """
        HS-SR04
        Return distance in cm
        """

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        zero = time.time()
        pulse_start = time.time()
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
            if pulse_start - zero > 0.1:
                return -1

        zero = time.time()
        pulse_end = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
            if pulse_end - zero > 0.1:
                return -1

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150

        if distance < 2:
            return -1

        return round(distance, 1)

    def distance(self):
        correct = False
        while not correct:
            dist = self.ping()
            if dist == -1 or dist < -1:
                continue
            correct = True
        return dist



if __name__ == "__main__":
    asdic = ASDIC()
    atexit.register(GPIO.cleanup)
    while 1:
        p = asdic.ping()
        print(asdic.ping())
        time.sleep(0.01)
