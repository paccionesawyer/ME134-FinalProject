#https://custom-build-robots.com/electronic/stepper-motor-28byj-48-uln2003a-controller-raspberry-pi-and-python/8862?lang=en
from time import sleep
import RPi.GPIO as GPIO

class miniStepper(object):

    #Initialize Stepper object
    def __init__(self,P1,P2,P3,P4):
        self.spin = ([0,0,0,1],[0,0,1,1],[0,0,1,0],[0,1,1,0],[0,1,0,0],[1,1,0,0],[1,0,0,0],[1,0,0,1])
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3
        self.P4 = P4
        self.angle = 0
        self.motor_channel = (P1,P2,P3,P4) 
        for pin in self.motor_channel:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)


    def turnAngleCW(self):
        self.setAllPinsLow()
        steps = int(wantedAngle/1.8)
        state = 0
        for i in range(steps):
            GPIO.output(self.motor_channel, self.spin[state])
            sleep(self.time)
            GPIO.output(self.motor_channel, [0,0,0,0]) #Check this
            state+=1
            if (state == 8):
                state = 0


    def turnAngleCCW(self):
        self.setAllPinsLow()
        steps = int(wantedAngle/(360/2048))
        state = 8
        for i in range(steps):
            GPIO.output(self.motor_channel, self.spin[state])
            sleep(self.time)
            GPIO.output(self.motor_channel, [0,0,0,0]) #Check this
            state-=1
            if (state == 0):
                state = 8

    def turnCW(self):
        try:
            state = 0
            while True:
                GPIO.output(self.motor_channel, self.spin[state])
                sleep(self.time)
                GPIO.output(self.motor_channel, [0,0,0,0]) #Check this
                state+=1
                if (state == 8):
                state = 0

        except KeyboardInterrupt:
            pass

    def turnCCW(self):
        try:
            state = 8
            while True:
                GPIO.output(self.motor_channel, self.spin[state])
                sleep(self.time)
                GPIO.output(self.motor_channel, [0,0,0,0]) #Check this
                state-=1
                if (state == 0):
                state = 8

        except KeyboardInterrupt:
            pass

    #Set all pins low
    def setAllPinsLow(self):
        GPIO.output(self.P1, 0)
        GPIO.output(self.P2, 0)
        GPIO.output(self.P3, 0)
        GPIO.output(self.P4, 0)

    def setSpeed(self, speed):
        self.time = (10.0 / self.speed)
		


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    motor = miniStepper(6,13,19,26)
    motor.setSpeed(100)
    motor.turnAngleCCW(90)
    GPIO.cleanup()