from blinking_light import __devenv__
if __devenv__:
    from blinking_light.my_fake_rpigio import fake_rpigio as GPIO
else:
    import RPi.GPIO as GPIO


class GpioBoard():
    
    portEnabled = False
    portNumber = 0
    portMode = None
    config = None
    portPowered = False

    def __init__(self, boardConfig):
        if boardConfig == "BCM":
            boardConfig = GPIO.BCM

        GPIO.setwarnings(False)
        GPIO.setmode(boardConfig)
        self.config = boardConfig

    def enablePort(self, portNumber, portMode):
        if portMode == "OUT":
            portMode = GPIO.OUT
        
        GPIO.setup(portNumber, portMode)
        self.portEnabled = True
        self.portNumber = portNumber
        self.portMode = portMode

    def powerOn(self):
        if self.portEnabled == True:
            GPIO.output(self.portNumber, True)
            self.portPowered = True

    def powerOff(self):
        if self.portPowered == True:
            GPIO.output(self.portNumber, False)
            self.portPowered = False

    def cleanUp(self):
        if self.portPowered == True:
            self.powerOff()
        GPIO.cleanup()
        self.portEnabled = False
        self.portNumber = 0
        self.portMode = None
        self.boardMode = None
