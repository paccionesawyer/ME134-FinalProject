# By: Ronan Gissler
# Adapted By: Sawyer Paccione... to include an encoder for the Polulu HPCB Micro Metal Gear Motor 6V
# Used on DC Micro Metal Gearmotor for ME134: Robotics
# with L298N Dual H-Bridge Motor Driver
# Motor product page here: 
# https://www.pololu.com/product/3062

# Simply setup the motor using the motor class constructor and then begin 
# calling the motor's set_speed and stop functions to move the motor in
# either direction

import RPi.GPIO as GPIO
import time

class Motor:
    def __init__(self, pin1, pin2, pinMode='BCM', freq=500):
        
        if pinMode == 'BCM':
            # using pin numbers (BCM) GPIO numbers for pin naming rather than (BOARD) 
            GPIO.setmode(GPIO.BCM)
        else:
            GPIO.setmode(GPIO.BOARD)
        
        # initializing pins as outputs
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        self.pin1 = pin1
        self.pin2 = pin2
        
        # setting up PWM channels on pins at specified frequency
        self.pwm1 = GPIO.PWM(pin1, freq) # for driving motor forward
        self.pwm2 = GPIO.PWM(pin2, freq) # for driving motor backward

    # set speed of motor where speed is defined as the PWM duty cycle
    def set_speed(self, speed):
        MAX_SPEED = 100
        self.stop() # avoid sending conflicting PWM signals at the same time
        if (speed > 0):
            # exceeding 60% duty cycle may burn out the 6V motor while
            # running at 7.4V
            if (speed > MAX_SPEED):
                self.pwm1.start(MAX_SPEED)
            else:
                self.pwm1.start(speed)
        elif (speed < 0):
            # exceeding 60% duty cycle may burn out the 6V motor while
            # running at 7.4V
            if (speed < -MAX_SPEED):
                self.pwm2.start(MAX_SPEED)
            else:
                self.pwm2.start(-speed)

    def test_cw(self):
        try:
            while True:
                GPIO.output(self.pin1, GPIO.HIGH)
                GPIO.output(self.pin2, GPIO.LOW)
        except KeyboardInterrupt:
            self.__del__()
            
    def stop(self):
        self.pwm1.stop()
        self.pwm2.stop()

    def __del__(self):
        GPIO.cleanup()   