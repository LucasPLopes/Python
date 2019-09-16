#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B,OUTPUT_D, SpeedPercent, MoveTank
from time import sleep


tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
gun = MediumMotor(OUTPUT_D)
def goforwad(robo, rotations):
    robo.on_for_rotations(SpeedPercent(100), SpeedPercent(100), rotations)

def goback(robo,rotations):
    robo.on_for_rotations(SpeedPercent(-100), SpeedPercent(-100), rotations)

def shoot(robo):
    robo.on_for_rotations(SpeedPercent(100),1)
    robo.on_for_rotations(SpeedPercent(100),-1)

def goleft(robo,rotations):
    robo.on_for_rotations(SpeedPercent(30), SpeedPercent(60), rotations)

def goright(robo,rotations):
    robo.on_for_rotations(SpeedPercent(60), SpeedPercent(30), rotations)

def gobleft(robo,rotations):
    robo.on_for_rotations(SpeedPercent(-30), SpeedPercent(-60), rotations)

def gobright(robo,rotations):
    robo.on_for_rotations(SpeedPercent(-60), SpeedPercent(-30), rotations)

def go180(robo):
    robo.on_for_rotations(SpeedPercent(-100), SpeedPercent(100), 5  )
goforwad(tank_drive, 3)
shoot(gun)
