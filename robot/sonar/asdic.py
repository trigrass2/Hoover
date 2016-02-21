#!/usr/bin/python3
#Anti-Submarine Division

import RPi.GPIO as GPIO
import time, atexit

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)

class ASDIC:
    
    def clean(self):
        GPIO.cleanup()
    
    def ping(self):
        """
        Return distance in cm
        """
        
        print("Distance measurement in progress...")
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        
        GPIO.output(TRIG, False)
        print("Waiting for sensor to settle")
        time.sleep(2)
        
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
            
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
            
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        
        GPIO.cleanup()
        
        return round(distance, 2)
        

if __name__ == "__main__":
    asdic = ASDIC()
    atexit.register(GPIO.cleanup)
    print(asdic.ping())
        
        
