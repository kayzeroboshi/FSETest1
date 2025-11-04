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

def distance():
    """ Measure the distance using the ultrasonic sensor """
    GPIO.output(motionPin, 0)
    time.sleep(0.000002)
    GPIO.output(motionPin, 1)
    time.sleep(0.00001)
    GPIO.output(motionPin, 0)

    while GPIO.input(motionPin) == 0:
        pass
    time1 = time.time()
    
    while GPIO.input(motionPin) == 1:
        pass
    time2 = time.time()

    duration = time2 - time1
    return (duration * 340 / 2) * 100  # Convert to centimeters

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
    
    """
    while True:
        dis = distance()
        print(dis, 'cm')  # Print distance measurement

        if dis < 5:  # If the object is within 5 cm, buzz continuously
            buzzer_on()
        elif dis < 30:  # If within 30 cm, beep with decreasing interval
            beep_interval = (dis - 5) / 50.0  # Adjust beep interval
            beep(beep_interval)
        else:
            buzzer_off()  # Turn off buzzer if object is far
        
        time.sleep(0.3)
    """

def destroy():
    """ Cleanup function to reset GPIO settings """
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    x=1
    while x==1:
        buzzer_on()
