#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

# Define GPIO pins
#TRIG = 11       # GPIO pin connected to Trig of Ultrasonic Sensor
#ECHO = 12       # GPIO pin connected to Echo of Ultrasonic Sensor
motionPin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motionPin, GPIO.IN)
time.sleep(10)

BuzzerPin = 11  # GPIO pin connected to Buzzer

def setup():
    """ Setup the GPIO pins for the ultrasonic sensor and buzzer """
    GPIO.setmode(GPIO.BOARD)
    
    # Setup for ultrasonic sensor
    #GPIO.setup(motionPin, GPIO.OUT)
    #GPIO.setup(motionPin, GPIO.IN)
    
    # Setup for buzzer
    GPIO.setup(BuzzerPin, GPIO.OUT)
    GPIO.output(BuzzerPin, GPIO.HIGH)
    #change!



def buzzer_on():
    """ Turn the buzzer on """
    GPIO.output(BuzzerPin, GPIO.LOW)

def buzzer_off():
    """ Turn the buzzer off """
    GPIO.output(BuzzerPin, GPIO.HIGH)

def beep(duration):
    """ Make the buzzer beep for a specified duration """
    buzzer_on()
    time.sleep(duration)
    buzzer_off()
    time.sleep(duration)

def loop():
    """ Main loop that checks the distance and controls the buzzer """
    
    try:
        while True:
            motion = GPIO.input(motionPin)
            print(motion)
            time.sleep(.1)
            if motion == 1:
                buzzer_on()
            elif motion == 0:
                buzzer_off()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('GPIO Good to Go')
    
    



if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        

