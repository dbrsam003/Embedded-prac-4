#!/usr/bin/python

import spidev
import time
import os
import sys

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
s0 = 0
s1 = 1
s2 = 2

GPIO.setup(s0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

spi = spidev.SpiDev()
spi.open(0,0)

#channel 0 = light sensor
#channel 1 = tempreture



def GetData(channel):
	adc = spi.xfer2([1,(8+channel)<<4,0])
	data = ((sdc[1]&3)<<8)+adc[2]
	return data

def ConvertVolts(data,places):
	volts = (data*3.3)/float(1023)
	volts = round(volts,places)
	return volts

channel = 0
delay = 0.5

try:
	while True:
		light_data = GetData(0)
		sensor_volt = ConvertVolts(sensor_data,2)
		time.sleep(delay)

except KeyboardInterrupt:
	spi.close()

