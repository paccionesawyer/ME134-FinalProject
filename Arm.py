# Tufts University, Fall 2021
# Palm.py
# By: Sawyer Paccione
# Completed: TBD
#
# Description: Controlling the DC Motor and Lidar in the Palm of a Robot

import time
from miniStepperClass import miniStepper
from adafruit_servokit import ServoKit
import adafruit_vl53l0x

#Create miniStepper object

class Arm:
    '''
    One of the Arms of the Brachiation Robot
    '''
    def __init__(self,stepperPins,servoPin):
        '''
        Initialize our arm
        '''
        #Initialize GPIO Mode
        GPIO.setmode(GPIO.BCM)

        #Initialize I2C bus and Lidar sensor
        i2c = busio.I2C(board.SCL, board.SDA)
        self.vl53 = adafruit_vl53l0x.VL53L0X(i2c)

        self.servoKit = ServoKit(channels=16)
        self.servoKit.servo[servoPin].angle = 0

        self.stepper = miniStepper(stepperPins)

        self._angle = 0
        self._dist  = 0

    def extend(self, turnAngle):
        self.stepperLeft.turnAngleCW(turnAngle)
        #palm grasp

    def retract(self, turnAngle):
        #palm release
        self.stepperLeft.turnAngleCCW(turnAngle)

    def locateBar(self):
        self.minDistance = 1000
        for i in range(len(self.distances)):
            if (distances[i]<minDist):
                self.minDistance = distances[i]
                index = i

        #add threshold distance
        self.servoKit.servo[servoPin].angle = self.angles[index]
        
    def distToDegree():
        '''
        Convert a distance that the arm needs to move, to the associated degs to turn the stepper motor
        '''
        deg = self.minDistance / 50 #Not sure this yes
        return deg
    
    def sweep(self):
        angle = 0
        self.distances = []
        self.angles = []
        for i in range(18):
            self.servoKit.servo[servoPin].angle = angle
            self.angles.append(angle)
            lidarReading = self.vl53.range
            self.distances.append(lidarReading)
            angle+=5
            time.sleep(0.2)
    
    def resetArm():
        self.servoKit.servo[servoPin].angle = 0
        #open and close palmn

    