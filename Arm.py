# Tufts University, Fall 2021
# Palm.py
# By: Sawyer Paccione
# Completed: TBD
#
# Description: Controlling the DC Motor and Lidar in the Palm of a Robot



class Arm:
    '''
    One of the Arms of the Brachiation Robot
    '''

    def __init__(self):
        '''
        Initialize our arm
        '''
        self._angle = 0
        self._dist  = 0

    def extend(self, distance=50):
        '''
        Extends the scissor lift
        '''

    def retract(self, distance=50):
        '''
        Retracts the scissor lift
        '''

    def distanceToDeg(self, distance):
        '''
        Convert a distance that the arm needs to move, to the associated degs to turn the stepper motor
        '''
        deg = distance / 50
        return deg

