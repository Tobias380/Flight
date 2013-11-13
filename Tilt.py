import sys
import os
import time
import math
from datetime import datetime, date
from Adafruit_LSM303DLHC import LSM303DLHC
from Adafruit_PWM_Servo_Driver import PWM
import RPi.GPIO as gpio


lsm = LSM303DLHC(0x19, 0x1E, False)
pwm = PWM(0x40, debug=True)
lsm.setTempEnabled(True)
pwm.setPWMFreq(60)

servoMin = 150  # Min pulse length out of 4096
servoMax = 620  # Max pulse length out of 4096
Range = servoMax-servoMin
Incr= Range/180

pwm.setPWM (1, 0, servoMax)
time.sleep(0.5)
pwm.setPWM (1, 0, servoMin)
time.sleep(0.5)



##def ReadTilt (self):
##    accel = lsm.readAccelerationsG()
##    #Calculate tilt in x
##    TiltX= degrees(acos(1/accel.x))
##    #Calculate tilt in y
##    #TiltY= degrees(acos(1/accel.Y))
##
##    return TiltX


    
try:
    while (True):
        accel = lsm.readAccelerationsG()
        print accel.x
        tiltx= accel.x
        #Calculate tilt in x
        tiltxinv = (tiltx/1)
        TiltRad= math.acos(tiltxinv)
        TiltDeg=math.degrees(TiltRad)
        print TiltDeg
        swing= int(servoMax-(Incr*TiltDeg))
        print swing
        pwm.setPWM (1, 0, swing )
        print 'Test'
        time.sleep(0.1)
except: KeyboardInterrupt
        
gpio.cleanup()




    
        
