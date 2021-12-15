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
        self.openL = 1
        self.openR = 1

    def moveLeftArm(self):
        self.leftArm.palm.open()
        self.openL = 1
        self.leftArm.sweep()
        self.leftArm.locateBar()
        self.degree = self.leftArm.distToDegree()
        self.leftArm.extend(self.degree)
        self.leftArm.palm.close()
        self.openL = 0

    def moveRightArm(self):
        self.rightArm.palm.open()
        self.openR = 1
        self.rightArm.sweep()
        self.rightArm.locateBar()
        self.degree = self.rightArm.distToDegree()
        self.rightArm.extend(self.degree)
        self.rightArm.palm.close()
        self.openR = 0

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
        self.openR = 0
        self.leftArm.resetArm()
        self.openL = 0

    def unhookLeft():
        self.leftArm.palm.open()
         self.openL = 0

    def unhookRight():
        self.rightArm.palm.open()
        self.openR = 0

    def teleoperation(self):
        while True:
            response = input("Hello Potential User! How would you like to control the motor? \nUse WASD to control the left arm and IJKL to control the right arm.")

            while response not in ['w','a','s','d','e','i','j','k','l','o','q']: 
                print("I don't recognize that answer...")
                response = input("Use one of the following keys - W, A, S, D, I, J, K, or L")

            if response == "w":
                self.rightArm.extend(10)

            elif response == "a":
                self.rightArm.sweepForward()
                
            elif response == "s":
                self.rightArm.retract(10)
                
            elif response == 'd':
                self.rightArm.sweepBack()
            
            elif response == 'e':
                if (self.openR = 1):
                    self.rightArm.palm.close()
                elif (self.openR = 0):
                    self.rightArm.palm.open()
                
            elif response == 'i':
                self.leftArm.extend(10)

            elif response == 'j':
                self.leftArm.sweepForward()

            elif response == 'k':
                self.leftArm.retract()

            elif response == 'l':
                self.leftArm.sweepBack()

            elif response == 'o':
                if (self.openL = 1):
                    self.leftArm.palm.close()
                elif (self.openL = 0):
                    self.leftArm.palm.open()

            elif response == 'q':
                break
    
if __name__ == "__main__":

    #Define Pins
    rightArmStepper = [6,13,19,26] 
    rightShoulder = 0
    rightPalm = 1
    leftArmStepper = [17,27,22,23]
    leftShoulder = 2
    leftPalm = 3

    monkeyBot = Monkey(rightArmStepper,rightShoulder,rightPalm,leftArmStepper,leftShoulder,leftPalm)
    time.sleep(1)

    response = input("Please choose a mode! T for teleoperation and A for Autonomous")

            while response not in ['t','a']: 
                print("I don't recognize that answer...")
                response = input("Use one of the following keys - (T) Teleoperation, (A) Autonomous")

            if response == "t":
                monkeyBot.teleoperation()

            elif response == "a":
                monkeyBot.unhookLeft()
                time.sleep(1)
                monkeyBot.moveLeftArm()
                time.sleep(1)
                monkeyBot.rightToLeftTransition()
                time.sleep(1)
                monkeyBot.unhookRight()
                time.sleep(1)
                monkeyBot.moveRightArm()
                time.sleep(1)
                monkeyBot.leftToRightTransition()
                time.sleep()







 

