#https://custom-build-robots.com/electronic/stepper-motor-28byj-48-uln2003a-controller-raspberry-pi-and-python/8862?lang=en
from time import sleep
import RPi.GPIO as GPIO

class miniStepper(object):

    #Initialize Stepper object
    def __init__(self,Pins):
        self.spin = ([0,0,0,1],[0,0,1,1],[0,0,1,0],[0,1,1,0],[0,1,0,0],[1,1,0,0],[1,0,0,0],[1,0,0,1])
        self.P1 = Pins[0]
        self.P2 = Pins[1]
        self.P3 = Pins[2]
        self.P4 = Pins[3]
        self.motor_channel = (P1,P2,P3,P4)
        self.time = 0.001
        for pin in self.motor_channel:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)


    def turnAngleCW(self, wantedAngle):
        self.setAllPinsLow()
        steps = int(wantedAngle*(4096/360))
        state = 0
        for i in range(steps):
            GPIO.output(self.motor_channel, self.spin[state])
            sleep(self.time)
            GPIO.output(self.motor_channel, [0,0,0,0]) #Check this
            state+=1
            if (state == 8):
                state = 0


    def turnAngleCCW(self, wantedAngle):
        self.setAllPinsLow()
        steps = int(wantedAngle*(4096/360))
        state = 7
        for i in range(steps):
            GPIO.output(self.motor_channel, self.spin[state])
            sleep(self.time)
            GPIO.output(self.motor_channel, [0,0,0,0]) #Check this
            state-=1
            if (state == -1):
                state = 7

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

    #For later
    def setSpeed(self, speed):
        self.time = 0.001
		

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    motor = miniStepper(6,13,19,26)
    motor.setSpeed(100)
    motor.turnAngleCW(360)
    GPIO.cleanup()