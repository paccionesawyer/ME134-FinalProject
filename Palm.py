# Tufts University, Fall 2021
# Palm.py
# By: Sawyer Paccione
# Completed: TBD
#
# Description: Controlling the DC Motor and Lidar in the Palm of a Robot

from electronics.DCMotorEncoder.DCMotor_encoder import DCMotorEncoder
import time 

class Palm:
    '''
    Controlling the DC Motor and Lidar in the Palm of a Robot
    '''

    def __init__(self):
        '''
        Initialize our palm
        '''

        self.motor = DCMotorEncoder(33, 32, 31, 29, 'BOARD')
        
        self._bestDist = 2500

        self._distance = None
        self._angle = 0

    def close(self):
        '''
        Close the Palm
        '''
        self.motor.run_to_position(self._bestDist)

    def open(self):
        '''
        Open the palm
        '''
        self.motor.run_to_position(0)

    @property
    def distance(self):
        print("Getting Distance Value")
        return self._distance

    @distance.setter
    def distance(self, value):
        print("Why are you setting the value of your Lidar")
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


if __name__ == "__main__":
    p = Palm()
    p.close()
    time.sleep(1)
    p.open()