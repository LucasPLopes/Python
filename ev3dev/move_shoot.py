#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B,OUTPUT_D, SpeedPercent, MoveTank
from time import sleep


tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
gun = MediumMotor(OUTPUT_D)
def goforwad(robo, rotations):
    for i in range(1,rotations):
        robo.on_for_rotations(SpeedPercent(100), SpeedPercent(100), i)
        time.sleep(i)

def shoot(robo):
    robo.on_for_rotations(SpeedPercent(100),1)
    robo.on_for_rotations(SpeedPercent(100),-1)

goforwad(tank_drive, 3)
shoot(gun)
