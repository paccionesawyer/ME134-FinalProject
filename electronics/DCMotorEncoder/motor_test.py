# By: Ronan Gissler
# Used on DC Micro Metal Gearmotor for ME134: Robotics
# with L298N Dual H-Bridge Motor Driver
# Motor product page here: 
# https://www.pololu.com/product/3062

# This example spins the motor forwards for 1 second and backwards for 1 second

import time
from DCMotor import Motor

pin1 = 16
pin2 = 18

launch_motor = Motor(pin1, pin2)

print("Backward at 100% duty cycle")
launch_motor.set_speed(-100)
time.sleep(5)
launch_motor.stop()

# time.sleep(1)
# 
# print("Backward at 100% duty cycle")
# launch_motor.set_speed(-100)
# time.sleep(1)
# launch_motor.stop()