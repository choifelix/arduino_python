from Arduino import Arduino
import time

class SR04:
    """class created for ultrasonic censor from arduino starterkit SR04"""

    def __init__(self, echo, trigger, board):
        self.echoPin    = echo
        self.triggerPin = trigger
        self.distance = 999
        board.pinMode(echo, 'INPUT')
        board.pinMode(trigger, 'OUTPUT')
        self.board = board

    def Distance(self):
        d = 0
        duration = 0
        self.board.digitalWrite(self.triggerPin, 'LOW')
        time.sleep(0.002)
        self.board.digitalWrite(self.triggerPin, 'HIGH')
        time.sleep(0.01)
        self.board.digitalWrite(self.triggerPin, 'LOW')
        time.sleep(0.002)
        duration = self.board.pulseIn(self.echoPin, 5000)
        d = self.MicrosecondsToCentimeter(duration)
        time.sleep(0.025)
        return d

    def MicrosecondsToCentimeter(self, duration):
        d = (duration *100) / 5882
        return d
		




        
