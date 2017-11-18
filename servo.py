import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

def run(bool):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    pwm = GPIO.PWM(25, 50)
    pwm.start(7.5)
    print("Mode : " + bool)
    if(bool == "1"):
        print("MODE1 ACTIVATED")
        pwm.ChangeDutyCycle(12.3) #-90
        time.sleep(2)
    elif(bool == "2"):
        print("MODE2 ACTIVATED")
        pwm.ChangeDutyCycle(2.7) # 90
        time.sleep(2)
    else:
        print("ALL DEACTIVATED")
        pwm.stop()  
        GPIO.cleanup()	
    


def main(bool):
    run(bool)

if __name__ == "__main__":
    main(sys.argv[1])
