import sys
import os
import time
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
Incr= Range/60

try:
    while (True):
         time.sleep(0.25)
         heading = lsm.readMagneticHeading()
         if (heading > 0):
             pwm.setPWM(1, 0, servoMin)
             print 'Positive'
         if (heading < 0):
             pwm.setPWM(1, 0, servoMax)
             print 'Negative'
         if (heading==0):   
             print 'facing north'
except: KeyboardInterrupt
gpio.cleanup()
             
             
