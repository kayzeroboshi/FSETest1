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
def setupIRBUZZZ():
    """ Setup the GPIO pins for the ultrasonic sensor and buzzer """
    GPIO.setmode(GPIO.BOARD)
    
    # Setup for ultrasonic sensor
    #GPIO.setup(motionPin, GPIO.OUT)
    #GPIO.setup(motionPin, GPIO.IN)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motionPin, GPIO.IN)
    time.sleep(10)
    
    # Setup for buzzer
    GPIO.setup(BuzzerPin, GPIO.OUT)
    GPIO.output(BuzzerPin, GPIO.HIGH)
    #change!


    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    # Setup for vibration motor
    GPIO.setup(VIBRATION_MOTOR, GPIO.OUT)
    GPIO.output(VIBRATION_MOTOR, GPIO.LOW)
    print("vibration setup module works")


"""
def setupULTRA_VI():
    
    #GPIO.setmode(GPIO.BOARD)

    # Setup for ultrasonic sensor
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    # Setup for vibration motor
    GPIO.setup(VIBRATION_MOTOR, GPIO.OUT)
    GPIO.output(VIBRATION_MOTOR, GPIO.LOW)  # Turn off the vibration motor initiall
    
"""


# Function to measure Distance
def distanceULTRA_VI():
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
    return (duration * 340 / 2) * 100  # Convert to centimeters

# Vibration Motor Control Functions
def vibrate_for_seconds(seconds=0.5):
    """ Activate the vibration motor for a specified number of seconds """
    GPIO.output(VIBRATION_MOTOR, GPIO.HIGH)  # Turn on the vibration motor
    time.sleep(seconds)  # Keep it on for the specified duration
    GPIO.output(VIBRATION_MOTOR, GPIO.LOW)  # Turn off the vibration motor
    print(" viabrate seconds module works ")


def buzzer_on():
    """ Turn the buzzer on """
    GPIO.output(BuzzerPin, GPIO.LOW) #GPIO.output(BuzzerPin, GPIO.LOW)

def buzzer_off():
    """ Turn the buzzer off """
    GPIO.output(BuzzerPin, GPIO.HIGH) #GPIO.output(BuzzerPin, GPIO.LOW)

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
            dis = distanceULTRA_VI()
            print(f"Object detected at: {dis} cm")
            print(" ultra violoet system works")

            #ir buzzer function 
            motion = GPIO.input(motionPin)
            print(motion)
            time.sleep(.1)
            print("buzzer system works")
            print("buzzer system works")
            print("buzzer system works")

            if dis < 50:  # If the distance is less than 20 cm
                vibrate_for_seconds(1)  # Vibrate for 0.5 seconds
                print("Hey shivan it works! it is being detected!")
            #time.sleep(0.3)
            #ir buzzer if stuff
            if motion == 1:
                #buzzer_on()
                #print("loop_buzzer on moule")
                beep(1)
            elif motion == 0:
                buzzer_off()
                print("loop buzzer off module")
            
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("GPIo Good to GO")

# Cleanup Function
def destroy():
    """ Cleanup function to reset GPIO settings """
    GPIO.cleanup()

# Running the Script
if __name__ == "__main__":
    # setupULTRA_VI()
    setupIRBUZZZ()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
