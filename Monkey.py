from Arm import*

rightArmStepper = [11,12,13,14] 


class Monkey:
    def __init__(self,rightArmStepper,rightShoulder,rightPalm,leftArmStepper,leftShoulder,leftPalm):
        self.rightArm = (rightArmStepper,rightShoulder,rightPalm)
        self.leftArm = (leftArmStepper,leftShoulder,leftPalm)

    def moveLeftArm():
        leftArm.sweep()
        leftArm.locateBar()
        self.degree = leftArm.distToDegree()
        leftArm.extend(degree)

    def moveRightArm():
        rightArm.sweep()
        rightArm.locateBar()
        self.degree = rightArm.distToDegree()
        rightArm.extend(degree)

    def leftToRightTransition():
        #extend left while contracting right
        self.midDegree = self.degree/2 
        for i in range(self.midDegree):
            leftArm.extend(1)
            rightArm.contract(1)

    def rightToLeftTransition():
        #extend right while contracting left
        self.midDegree = self.degree/2 
        for i in range(self.midDegree):
            rightArm.extend(1)
            leftArm.contract(1)

    def reset():
        rightArm.resetArm()
        leftArm.resetArm()
    


 

