from Arm import Arm 

rightArmStepper = [11,12,13,14] 


class Monkey:
    def __init__(self,rightArmStepper,rightShoulder,rightPalm,leftArmStepper,leftShoulder,leftPalm):
        self.rightArm = (rightArmStepper,rightShoulder,rightPalm)
        self.leftArm = (leftArmStepper,leftShoulder,leftPalm)

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
    


 

