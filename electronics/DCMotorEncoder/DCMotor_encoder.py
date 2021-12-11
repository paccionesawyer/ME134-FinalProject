# By: Ronan Gissler
# Used on DC Micro Metal Gearmotor for ME134: Robotics
# with L298N Dual H-Bridge Motor Driver
# Motor product page here: 
# https://www.pololu.com/product/3062

# Simply setup the motor using the motor class constructor and then begin 
# calling the motor's set_speed and stop functions to move the motor in
# either direction

import RPi.GPIO as GPIO
import time

class DCMotorEncoder:
    # With a 1000:1 gear ratio on the motor and a CPR of 12, there are 
    # 12000 ticks per revolution of the motor shaft.
    ticksPerRev = 12000

    def __init__(self, motor_pin1, motor_pin2, encoder_pin1, encoder_pin2, pinMode='BOARD', freq=50):
        
        if pinMode == 'BOARD':
            # using pin numbers (BOARD) rather than GPIO numbers (BCM) for pin naming
            GPIO.setmode(GPIO.BOARD) 
        else:
            GPIO.setmode(GPIO.BCM) 
        
        # initializing motor pins as outputs
        GPIO.setup(motor_pin1, GPIO.OUT)
        GPIO.setup(motor_pin2, GPIO.OUT)

        # Declaring pin modes for encoder hall effect sensors. Since the hall effect
        # sensors have built-in hysteresis control, INPUT_PULLUP is not required
        GPIO.setup(encoder_pin1, GPIO.IN)
        GPIO.setup(encoder_pin2, GPIO.IN)

        # The position of the motor shaft in ticks
        self.num_ticks = 0
        
        # setting up PWM channels on pins at specified frequency
        self.encoder_pin1 = encoder_pin1
        self.encoder_pin2 = encoder_pin2
        self.pwm1 = GPIO.PWM(motor_pin1, freq) # for driving motor forward
        self.pwm2 = GPIO.PWM(motor_pin2, freq) # for driving motor backward

    # set speed of motor where speed is defined as the PWM duty cycle
    def set_speed(self, speed):
        self.stop() # avoid sending conflicting PWM signals at the same time
        if (speed > 0):
            # exceeding 60% duty cycle may burn out the 6V motor while
            # running at 7.4V
            if (speed > 60):
                self.pwm1.start(60)
            else:
                self.pwm1.start(speed)
        elif (speed < 0):
            # exceeding 60% duty cycle may burn out the 6V motor while
            # running at 7.4V
            if (speed < -60):
                self.pwm2.start(60)
            else:
                self.pwm2.start(-speed)
            
    def stop(self):
        self.pwm1.stop()
        self.pwm2.stop()

    def count_ticks(self):
        # Encoder state variables. There are 2 Hall Effect Sensors, 
        # each with a past and current state 
        self.lastStateOne
        self.lastStateTwo

        curStateOne = GPIO.input(self.encoder_pin1)
        curStateTwo = GPIO.input(self.encoder_pin2)
      
        # Counting ticks on quadrature encoders
        if ((self.lastStateOne!=curStateOne) and (curStateOne!=curStateTwo)):
            self.lastStateOne = curStateOne
            self.num_ticks = self.num_ticks + 1
        elif ((self.lastStateOne!=curStateOne) and (curStateOne==curStateTwo)):
            self.lastStateOne = curStateOne
            self.num_ticks = self.num_ticks - 1 # motors moving in reverse
        elif ((self.lastStateTwo!=curStateTwo) and (curStateTwo==curStateOne)):
            self.lastStateTwo = curStateTwo
            self.num_ticks = self.num_ticks + 1
        elif ((self.lastStateTwo!=curStateTwo) and (curStateTwo!=curStateOne)):
            self.lastStateTwo = curStateTwo
            self.num_ticks = self.num_ticks - 1 # motors moving in reverse

    def run_to_position(self, des_ticks):
        stalled = False

        while ((abs(self.num_ticks) < abs(des_ticks)) and not stalled):
            init_time = time.time() * 1000 # record the initial time of the inner while loop in ms
            init_ticks = self.num_ticks
            
            while(((time.time() * 1000) - init_time) < 50): # after 50 ms
                if (abs(self.num_ticks) < abs(des_ticks)):
                    self.count_ticks()
                else:
                    self.stop() # stop motor, desired position reached

            # Are motors stalling (less than 70 ticks in 50 ms)?
            if ((abs(self.num_ticks) < abs(des_ticks)) and ((self.num_ticks - init_ticks) < 70)):
                self.stop() # stop motor, motors are stalling
                stalled = True

    def runAtSpeed(self, speed):
        '''
        Turn on motor with given speed.
        '''
        pass 

    def runForDegrees(self, degrees):
        '''
        Turn motor a given number of degrees from current position
        '''
        pass 

    def runForTime(self, time, speed):
        '''
        Turn on motor for given time with given speed
        '''
        pass 

    def stop(self):
        '''
        Stops the Motor
        '''
        self.runAtSpeed(0)

    def __del__(self):
        GPIO.cleanup()

    @property
    def num_ticks(self):
        print("Getting Angle Value")
        return self._num_ticks

    @num_ticks.setter
    def num_ticks(self, value):
        self._num_ticks = value

    @num_ticks.deleter
    def num_ticks(self):
        del self._num_ticks