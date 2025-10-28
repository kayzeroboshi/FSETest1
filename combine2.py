import RPi.GPIO as GPIO #suo apt update  # sudo apt install python3-rpi.gpio
import time #

# Definitions
TRIG = 11       # GPIO pin for Trig of Ultrasonic Sensor
ECHO = 12       # GPIO pin for Echo of Ultrasonic Sensor
VIBRATION_MOTOR = 15  # GPIO pin for Vibration Motor 

motionPin = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motionPin, GPIO.IN)
time.sleep(10)

BuzzerPin = 13  # GPIO pin connected to Buzzer

# GPIO Setup
def setup():
    """ Setup the GPIO pins for the ultrasonic sensor and vibration motor """
    GPIO.setmode(GPIO.BOARD)

    # Setup for ultrasonic sensor
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    # Setup for vibration motor
    GPIO.setup(VIBRATION_MOTOR, GPIO.OUT)
    GPIO.output(VIBRATION_MOTOR, GPIO.LOW)  # Turn off the vibration motor initiall


    """ Setup the GPIO pins for the ultrasonic sensor and buzzer """
    GPIO.setmode(GPIO.BOARD)
    
    # Setup for ultrasonic sensor
    #GPIO.setup(motionPin, GPIO.OUT)
    #GPIO.setup(motionPin, GPIO.IN)
    
    # Setup for buzzer
    GPIO.setup(BuzzerPin, GPIO.OUT)
    GPIO.output(BuzzerPin, GPIO.HIGH)

# Function to measure Distance
def distance():
    """ Measure the distance using the ultrasonic sensor """
    GPIO.output(TRIG, 0)
    time.sleep(0.000002)
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0: #0
        pass
    time1 = time.time()
    
    while GPIO.input(ECHO) == 1: # 1
        pass
    time2 = time.time()

    duration = time2 - time1
    #return (duration * 340 / 2) * 100  # Convert to centimeters
    # blah blah 
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

    #duration1 = time2 - time1
    return (duration * 340 / 2) * 100  # Convert to centimeters

# Vibration Motor Control Functions
def vibrate_for_seconds(seconds=0.5):
    """ Activate the vibration motor for a specified number of seconds """
    GPIO.output(VIBRATION_MOTOR, GPIO.HIGH)  # Turn on the vibration motor
    time.sleep(seconds)  # Keep it on for the specified duration
    GPIO.output(VIBRATION_MOTOR, GPIO.LOW)  # Turn off the vibration motor


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

# Main Loop for Distance Monitoring
def loop():
    """ Main loop that checks the distance and controls the vibration motor """
        
    try:
        while True:
            dis = distance()
            print(f"Object detected at: {dis} cm")

            #ir buzzer function 
            motion = GPIO.input(motionPin)
            print(motion)
            time.sleep(.1)

            if dis < 30:  # If the distance is less than 20 cm
                vibrate_for_seconds(0.5)  # Vibrate for 0.5 seconds
            time.sleep(0.3)
            #ir buzzer if stuff
            if motion == 1:
                buzzer_on()
            elif motion == 0:
                buzzer_off()
            
            
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("GPIo Good to GO")

# Cleanup Function
def destroy():
    """ Cleanup function to reset GPIO settings """
    GPIO.cleanup()

# Running the Script
if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
