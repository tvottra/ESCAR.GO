#!/usr/bin/python

import PiMotor
import time
import RPi.GPIO as GPIO

#Name of Individual MOTORS 
m1 = PiMotor.Motor("MOTOR1",2)
m2 = PiMotor.Motor("MOTOR2",2)
m3 = PiMotor.Motor("MOTOR3",2)
m4 = PiMotor.Motor("MOTOR4",2)

#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)

#Names for Individual Arrows
ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3) 
ar = PiMotor.Arrow(4)

##This segment drives the motors in the direction listed below:
## forward and reverse takes speed in percentage(0-100)
m1.forward(40)
time.sleep(3)
    
