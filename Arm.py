# Tufts University, Fall 2021
# Palm.py
# By: Sawyer Paccione, Olivia Tomassetti, Rónán Gissler
# Completed: TBD
#
# Description: Controlling the DC Motor and Lidar in the Palm of a Robot

import time
import board
import busio
from electronics.miniStepperClass import miniStepper
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
from Palm import Palm
import math

#Create miniStepper object

class Arm:
    '''
    One of the Arms of the Brachiation Robot
    '''
    def __init__(self, stepperPins=[6,13,19,26], shldrPin=0, palmPin=1):
        '''
        Initialize our arm
        '''
        #Initialize GPIO Mode
        GPIO.setmode(GPIO.BCM)

        # Initialize I2C bus and Lidar sensor
        # i2c = busio.I2C(board.SCL, board.SDA)
        # self.vl53 = adafruit_vl53l0x.VL53L0X(i2c) # Moved this code to be in the palm

        self.servoKit = ServoKit(channels=16)
        self.shldrServo = self.servoKit.servo[shldrPin]
        
        self.shldrServo.angle = 0

        self.stepper = miniStepper(stepperPins)

        self._angle = 0
        self._length  = 0

        self.minDistance = 1000
        
        self.link_length = 70 
        # ^ in mm, between circle centers at link ends along link axis
        self.link_horizontal_dist = 67
        # ^ in mm, horizontal distance between circle centers at link ends
        self.num_links = 4
        self.pinion_diameter = 16 # also in mm

        # TODO dynamically change palm shldrPin
        self.palm = Palm(palmPin, self.servoKit)

    def extend(self, turnAngle):
        self.stepper.turnAngleCW(turnAngle)
        self.palm.close()
        #palm grasp

    def retract(self, turnAngle):
        #palm release
        self.palm.open()
        self.stepper.turnAngleCCW(turnAngle)

    def locateBar(self):
        self.minDistance = 1000
        for i in range(len(self.distances)):
            if (self.distances[i] < self.minDistance):
                self.minDistance = self.distances[i]
                index = i

        # add threshold distance
        self.shldrServo.angle = self.angles[index]
        
    def distToDegree(self):
        '''
        Convert a distance that the arm needs to move, to the associated degs to turn the stepper motor
        '''
        self.minDistance = 20
        print("minDistance: ", self.minDistance)
        distance_per_link = self.minDistance / self.num_links
        print("distance_per_link", distance_per_link)
        horizontal_distance = (math.cos(math.asin(distance_per_link / self.link_length))*(180/math.pi) * self.link_length)
        print("horizontal_distance", horizontal_distance)
        deg = horizontal_distance / (math.pi * self.pinion_diameter)
        

        if(deg > 400):
            print("Distance to big: ", deg)
            return 0

        print("Degree: ", deg)
        return deg
    
    def sweep(self):
        '''
        Sweep the arm up an down, getting servo angles along the ways,
        '''
        self.angle = 0
        self.distances = []
        self.angles = []
        for i in range(18):
            self.shldrServo.angle = self.angle
            self.angles.append(self.angle)
            lidarReading = self.palm.distance
            self.distances.append(lidarReading)
            self.angle += 5
            time.sleep(0.2)
    
    def resetArm(self):
        '''
        Set the arm back to it's default state
        '''
        self.shldrServo.angle = 0
        #open and close palm
        self.palm.open()
        self.palm.close()



    @property
    def angle(self):
        #print("Getting Palm Angle Value")
        return self._angle

    @angle.setter
    def angle(self, value):
        # print(value, type(value))
        if not isinstance(value, int):
            msg = "Angle should be an integer value instead got: " + str(value) + ' ' + str(type(value))
            raise ValueError(msg)
        elif value < 0:
            raise ValueError("Angle Below 0 is Impossible")
        elif value > 180:
            raise ValueError("Angle Above 180 is Impossible")
        else:
            self._angle = value

    @angle.deleter
    def angle(self):
        del self._angle


if __name__ == "__main__":
    army = Arm([6,13,19,26],0)
    army.distToDegree()
    # while True:
    #     army.sweep()
    #     army.locateBar()
    #     wait = input("Press Enter To Redo")
    #     army.resetArm()
    #     time.sleep(3)
'''
    while True:
        dist = int(input("How far would you like to move?"))
        army.extend(dist)
        time.sleep(.2)
        army.retract(dist)
'''
