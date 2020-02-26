#!/usr/bin/env python
"""
 Blinks an LED on digital pin 13
 in 1 second intervals
"""

from Arduino import Arduino
import time
							 #/dev/ttyACM0 for linux
board = Arduino('9600', port="/dev/cu.usbmodem141201") #plugged in via USB, serial com at rate 9600
board.pinMode(13, "OUTPUT")

iter_ = 0
while(True):
	board.digitalWrite(13, "LOW")
	time.sleep(2)
	board.digitalWrite(13, "HIGH")
	time.sleep(2)
	iter_ += 1
	print( iter_)
