# Tufts University, Fall 2021
# Palm.py
# By: Sawyer Paccione, Olivia Tomassetti
# Completed: TBD
#
# Description: Controlling the DC Motor and Lidar in the Palm of a Robot

import time
from electronics.miniStepperClass import miniStepper
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
from Palm import Palm

#Create miniStepper object

class Arm:
    '''
    One of the Arms of the Brachiation Robot
    '''
    def __init__(self, stepperPins=[26,19,13,5], servoPin=0):
        '''
        Initialize our arm
        '''
        #Initialize GPIO Mode
        GPIO.setmode(GPIO.BCM)

        # Initialize I2C bus and Lidar sensor
        # i2c = busio.I2C(board.SCL, board.SDA)
        # self.vl53 = adafruit_vl53l0x.VL53L0X(i2c) # Moved this code to be in the palm

        self.servoKit = ServoKit(channels=16)
        self.servoKit.servo[servoPin].angle = 0

        self.stepper = miniStepper(stepperPins)

        self._angle = 0
        self._length  = 0

        # TODO dynamically change palm servopin
        self.palm = Palm(3, self.servoKit)

    def extend(self, turnAngle):
        self.stepperLeft.turnAngleCW(turnAngle)
        self.palm.close()
        #palm grasp

    def retract(self, turnAngle):
        #palm release
        self.palm.open()
        self.stepperLeft.turnAngleCCW(turnAngle)

    def locateBar(self):
        self.minDistance = 1000
        for i in range(len(self.distances)):
            if (self.distances[i] < self.minDist):
                self.minDistance = self.distances[i]
                index = i

        # add threshold distance
        self.servoKit.servo[self.servoPin].angle = self.angles[index]
        
    def distToDegree(self, distance):
        '''
        Convert a distance that the arm needs to move, to the associated degs to turn the stepper motor
        '''
        deg = self.minDistance / 50 # Not sure of this yet Ronan Did Math
        return deg
    
    def sweep(self):
        '''
        Sweep the arm up an down, getting servo angles along the ways,
        '''
        angle = 0
        self.distances = []
        self.angles = []
        for i in range(18):
            self.servoKit.servo[self.servoPin].angle = angle
            self.angles.append(angle)
            lidarReading = self.palm._distance
            self.distances.append(lidarReading)
            angle += 5
            time.sleep(0.2)
    
    def resetArm(self):
        '''
        Set the arm back to it's default state
        '''
        self.servoKit.servo[self.servoPin].angle = 0
        #open and close palm
        self.palm.open()
        self.palm.close()

    @property
    def angle(self):
        print("Getting Arm Angle Value")
        return self._angle

    @angle.setter
    def angle(self, value):
        if isinstance(value, int):
            raise ValueError("angle should be an integer value")
        elif value < 0:
            raise ValueError("Angle Below 0 is Impossible")
        elif value > 180:
            raise ValueError("Angle Above 180 is Impossible")
        else:
            self._angle = value
            self.servoKit.servo[self.servoPin].angle = 0

    @angle.deleter
    def angle(self):
        del self._angle

    @property
    def length(self):
        print("Getting Length Value")
        return self._length

    @length.setter
    def length(self, value):
        if isinstance(value, int):
            raise ValueError("Distance should be an integer value")
        elif value < 0:
            raise ValueError("Distance below 0 is impossible")
        elif value > 10000:
            raise ValueError("Your Distance Sensor is Messed Up Sir")
        else:
            self._length = value

    @length.deleter
    def length(self):
        del self._length

if __name__ == "__main__":
    army = Arm()

    # while True:
    #     army.sweep()
    #     army.locateBar()
    #     wait = input("Press Enter To Redo")
    #     army.resetArm()
    #     time.sleep(3)

    while True:
        dist = int(input("How far would you like to extend?"))
        army.extend(army.distToDegree(dist))