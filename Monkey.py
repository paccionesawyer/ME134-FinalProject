# Tufts University, Fall 2021
# Monkey.py
# By: Sawyer Paccione, Olivia Tomassetti
# Completed: TBD
#
# Description: Controlling the the Arm Class

from Arm import Arm 
import time

class Monkey:
    def __init__(self,rightArmStepper,rightShoulder,rightPalm,leftArmStepper,leftShoulder,leftPalm):
        self.rightArm = Arm(rightArmStepper,rightShoulder,rightPalm)
        self.leftArm = Arm(leftArmStepper,leftShoulder,leftPalm)

    def moveLeftArm(self):
        self.leftArm.sweep()
        self.leftArm.locateBar()
        self.degree = self.leftArm.distToDegree()
        self.leftArm.extend(self.degree)

    def moveRightArm(self):
        self.rightArm.sweep()
        self.rightArm.locateBar()
        self.degree = self.rightArm.distToDegree()
        self.rightArm.extend(self.degree)

    def leftToRightTransition(self):
        #extend left while contracting right
        self.midDegree = self.degree/2 
        for i in range(self.midDegree):
            self.leftArm.extend(1)
            self.rightArm.contract(1)

    def rightToLeftTransition(self):
        #extend right while contracting left
        self.midDegree = self.degree/2 
        for i in range(self.midDegree):
            self.rightArm.extend(1)
            self.leftArm.contract(1)

    def reset(self):
        self.rightArm.resetArm()
        self.leftArm.resetArm()
    
if __name__ == "__main__":
    rightArmStepper = [6,13,19,26] 
    rightShoulder = 0
    rightPalm = 1
    leftArmStepper = [17,27,22,23]
    leftShoulder = 2
    leftPalm = 3
    
    monkeyBot = Monkey(rightArmStepper,rightShoulder,rightPalm,leftArmStepper,leftShoulder,leftPalm)
    #monkeyBot.reset()
    time.sleep(1)
    monkeyBot.moveRightArm()
    time.sleep(1)





 

