from blinking_light import __devenv__
if __devenv__:
    from blinking_light.my_fake_rpigio import fake_rpigio as GPIO
else:
    import RPi.GPIO as GPIO


class GpioBoard():
    
    portEnabled = False
    portNumber = 0
    portMode = None
    boardMode = None


    def __init__(self, boardMode):
        if boardMode == "BCM":
            boardMode = GPIO.BCM

        GPIO.setwarnings(False)
        GPIO.setmode(boardMode)
        self.boardMode = boardMode

    def enablePort(self, portNumber, portMode):
        if portMode == "OUT":
            portMode = GPIO.OUT
        
        GPIO.setup(portNumber, portMode)
        self.portEnabled = True
        self.portNumber = portNumber
        self.portMode = portMode
