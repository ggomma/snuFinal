import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

#pwm1 = GPIO.PWM(23, hz)
#pwm2 = GPIO.PWM(24, hz)


def run(bool):
    print("Mode : " + bool)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    if(bool == "1"):
        print("MODE1 ACTIVATED")
        GPIO.output(23, True)
        GPIO.output(24, False)
    elif(bool == "2"):
        print("MODE2 ACTIVATED")
        GPIO.output(23, False)
        GPIO.output(24, True)
    else:
        print("ALL DEACTIVATED")
        GPIO.cleanup()	
    


def main(bool):
    run(bool)

if __name__ == "__main__":
    main(sys.argv[1])
