import RPi.GPIO as GPIO
import time

class CircuitController():

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        self.canBlink = False

    def startBlink(self):
        self.canBlink = True
        thread = threading.Thread(target=self._blink, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()

    def _blink(self):
        while self.canBlink == True:
            GPIO.output(18, True)
            time.sleep(1)
            GPIO.output(18, False)
            time.sleep(1)

    def stopBlink(self):
        self.canBlink = False

    def blinkFor(self, secondsToBlink):
        self.startBlink()
        time.sleep(secondsToBlink)
        self.stopBlink()