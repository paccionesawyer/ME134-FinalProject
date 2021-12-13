# Tufts University, Fall 2021
# Palm.py
# By: Sawyer Paccione
# Completed: TBD
#
# Description: Controlling the Stepper Motor and Lidar in the Palm of a Robot

import time 
import board
import busio
from adafruit_servokit import ServoKit

import adafruit_vl53l0x

class Palm:
    '''
    Controlling the Servo Motor and Lidar in the Palm of a Robot
    '''

    def __init__(self, servoPin=0, servoKit=ServoKit(channels=16)):
        '''
        Initialize our palm
        '''
        # Initialize Servo Motor That will be controlling Open/Close
        self.servoKit = servoKit # Should be provided from a parent class
        self.fingers = self.servoKit.servo[servoPin] # Set Finger Servo
        self._angle = 1 #

        self.closedAngle = 90
        self.openAngle = 0
        
        # Initialize the lidar TOF sensor
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.vl53 = adafruit_vl53l0x.VL53L0X(self.i2c)
        self._distance = self.vl53.range

    def close(self):
        '''
        Close the Palm
        '''
        # print("close")
        self.angle = 0
        currAngle = self.angle
        for i in range(currAngle, self.closedAngle, 2):
            self.angle = i
            time.sleep(0.1)

    def open(self):
        '''
        Open the palm
        '''
        # print("open")
        currAngle = self.angle
        for i in range(currAngle, self.openAngle, -2):
            self.angle = i
            time.sleep(0.05)

    @property
    def distance(self):
        print("Getting Distance Value")
        self._distance = self.vl53.range
        return self._distance

    @distance.setter
    def distance(self, value):
        # print(value, type(value))
        if isinstance(int(value), int):
            msg = "Distance should be an integer value instead got:" + str(value) + ' ' + str(type(value))
            raise ValueError(msg)
        elif value < 0:
            raise ValueError("Distance below 0 is impossible")
        elif value > 10000:
            raise ValueError("Your Distance Sensor is Messed Up Sir")
        else:
            self._distance = value

    @distance.deleter
    def distance(self):
        del self._distance

    @property
    def angle(self):
        #print("Getting Palm Angle Value")
        return self._angle

    @angle.setter
    def angle(self, value):
        
        if not isinstance(value, int):
            msg = "Angle should be an integer value instead got: " + str(value) + ' ' + str(type(value))
            raise ValueError(msg)
        elif value < 0:
            raise ValueError("Angle Below 0 is Impossible")
        elif value > 180:
            raise ValueError("Angle Above 180 is Impossible")
        else:
            self._angle = value
            self.fingers.angle = self.angle

    @angle.deleter
    def angle(self):
        del self._angle


if __name__ == "__main__":
    p = Palm()

    while True:
        print("Closing Palm")
        p.close()
        print(p._angle)
        time.sleep(5)
        print("Opening Palm")
        p.open()
        print(p._angle)
        time.sleep(5)
