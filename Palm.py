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
    Controlling the DC Motor and Lidar in the Palm of a Robot
    '''

    def __init__(self, servoPin=0, servoKit=ServoKit(channels=16)):
        '''
        Initialize our palm
        '''
        # Initialize Servo Motor That will be controlling Open/Close
        self.servoKit = servoKit # Should be provided from a parent class
        self.fingers = self.servoKit.servo[servoPin] # Set Finger Servo
        self._angle = 0 #
        
        # Initialize the lidar TOF sensor
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.vl53 = adafruit_vl53l0x.VL53L0X(self.i2c)
        self._distance = self.vl53.range

    def close(self):
        '''
        Close the Palm
        '''
        self._angle = 0

    def open(self):
        '''
        Open the palm
        '''
        self._angle = 90

    @property
    def distance(self):
        print("Getting Distance Value")
        self._distance = self.vl53.range
        return self._distance

    @distance.setter
    def distance(self, value):
        if isinstance(value, int):
            raise ValueError("Distance should be an integer value")
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
        print("Getting Angle Value")
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
            self.fingers.angle = self._angle

    @angle.deleter
    def angle(self):
        del self._angle


if __name__ == "__main__":
    p = Palm()

    while True:
        print("Closing Palm")
        p.close()
        print(p._angle)
        time.sleep(1)
        print("Opening Palm")
        print(p._angle)
        p.open()
        time.sleep(1)
