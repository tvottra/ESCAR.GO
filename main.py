#!/usr/bin/python
from Getch import getch
import PiMotor
import time
import RPi.GPIO as GPIO

# Name of Individual MOTORS
frontLeft = PiMotor.Motor("MOTOR1", 2)
backLeft = PiMotor.Motor("MOTOR3", 2)
frontRight = PiMotor.Motor("MOTOR2", 2)
backRight = PiMotor.Motor("MOTOR4", 2)

# To drive all motors together
motorAll = PiMotor.LinkedMotors(frontLeft, backLeft, frontRight, backRight)

# Names for Individual Arrows
ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3)
ar = PiMotor.Arrow(4)

default_speed = 40
##This segment drives the motors in the direction listed below:
## forward and reverse takes speed in percentage(0-100)

def forward(speed = default_speed, tf = 1000):
    motorAll.forward(speed)
    time.sleep(tf)
    motorAll.stop()

def reverse(speed = default_speed, tf = 1000):
    motorAll.reverse(speed)
    time.sleep(tf)
    motorAll.stop()

def left(speed = default_speed, tf = 1000):
    frontRight.forward(default_speed)
    backRight.forward(default_speed)
    frontLeft.forward(default_speed * 0.5)
    backLeft.forward(default_speed * 0.5)
    time.sleep(tf)
    motorAll.stop()

def right(speed = default_speed, tf = 1000):
    frontLeft.forward(default_speed)
    backLeft.forward(default_speed)
    frontRight.forward(default_speed * 0.5)
    backRight.forward(default_speed * 0.5)
    time.sleep(tf)
    motorAll.stop()

def rotate_right(speed = default_speed, tf = 1000):
    frontLeft.forward(default_speed)
    backLeft.forward(default_speed)
    frontRight.reverse(default_speed)
    backRight.reverse(default_speed)
    time.sleep(tf)
    motorAll.stop()

def rotate_left(speed = default_speed, tf = 1000):
    frontLeft.reverse(default_speed)
    backLeft.reverse(default_speed)
    frontRight.forward(default_speed)
    backRight.forward(default_speed)
    time.sleep(tf)
    motorAll.stop()

try:
    command = 'u'
    while command != 'p':
        command = getch()
        command = command.lower()
        if command == 'w':
            forward(default_speed, 1)
        elif command == 's':
            reverse(default_speed, 1)
        elif command == 'a':
            left(default_speed, 1)
        elif command == 'd':
            right(default_speed, 1)
        elif command == 'q':
            rotate_left(default_speed, 0.3)
        elif command == 'e':
            rotate_right(default_speed, 0.3)
    motorAll.stop()
# -------------------------------------------------#

except KeyboardInterrupt:
    motorAll.stop()
    GPIO.cleanup()
