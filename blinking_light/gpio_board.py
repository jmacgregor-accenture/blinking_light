from blinking_light import __devenv__
if __devenv__:
    from blinking_light.my_fake_rpigio import fake_rpigio as GPIO
else:
    import RPi.GPIO as GPIO


class GpioBoard():
    
    config = None
    ports = []

    def __init__(self, boardConfig):
        if boardConfig == "BCM":
            boardConfig = GPIO.BCM

        GPIO.setwarnings(False)
        GPIO.setmode(boardConfig)
        self.config = boardConfig

    def addPort(self, port):
        self.ports.append(port)

    def cleanUp(self):
        for port in self.ports:
            port.cleanUp()
            
        GPIO.cleanup()
        self.config = None
