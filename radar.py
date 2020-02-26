#!/usr/bin/env python
from Arduino import Arduino
import time
from sr04 import SR04

if __name__ == '__main__':
    
    board = Arduino('9600', port="/dev/ttyACM0")
    # if your arduino was running on a serial port other than '/dev/ttyACM0/'
    # declare: a = Arduino(serial_port='/dev/ttyXXXX')

    time.sleep(3)
    # sleep to ensure ample time for computer to make serial connection 

    RED = 2
    GREEN = 3
    TRIGGER = 8
    ECHO = 9
    board.pinMode(RED,'OUTPUT')
    board.pinMode(GREEN,'OUTPUT')
	
    # initialize the digital pin as output
    sonicSensor = SR04(ECHO, TRIGGER, board)
	 

    time.sleep(1)
    # allow time to make connection
	
    distance = 999
    while(True):
        distance = sonicSensor.Distance()
        
        if ( distance != 0.0):
            print (distance)
            if ( distance >= 30 ):
                board.analogWrite(GREEN, 50)
                board.digitalWrite(RED, 'LOW')
            elif ( distance < 30 ):
                board.digitalWrite(GREEN, 'LOW')
                board.analogWrite(RED, 50)








