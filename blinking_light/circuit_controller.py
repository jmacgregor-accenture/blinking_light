import RPi.GPIO as GPIO
import time
import threading

class CircuitController():

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        self.canBlink = False
        self.timeOn = 1
        self.timeOff = 1


    def startBlink(self):
        self.canBlink = True
        thread = threading.Thread(target=self._blink, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()

    def adjustOnTime(self, newTime):
        self.timeOn = int(newTime)

    def adjustOffTime(self, newTime):
        self.timeOff = int(newTime)

    def _blink(self):
        while self.canBlink == True:
            self.powerOn()
            time.sleep(self.timeOn)
            self.powerOff()
            time.sleep(self.timeOff)
            
    def powerOn(self):
        GPIO.output(18, True)
        
    def powerOff(self):
        GPIO.output(18, False)

    def stopBlink(self):
        self.canBlink = False

    def blinkFor(self, secondsToBlink):
        timer = int(secondsToBlink)
        self.startBlink()
        time.sleep(timer)
        self.stopBlink()
