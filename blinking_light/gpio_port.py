from blinking_light import __devenv__
if __devenv__:
    from blinking_light.my_fake_rpigio import fake_rpigio as GPIO
else:
    import RPi.GPIO as GPIO


class GpioPort():

    portNumber = None
    portConfig = None
    isEnabled = None

    def __init__(self, portNumber, config):
        self.portNumber = portNumber
        self.portConfig = self._getGpioConfig(config)
        self._enablePort()

    def _getGpioConfig(self, config):
        if str(config).lower() == "out":
            return GPIO.OUT

    def _enablePort(self):
        if self.portNumber != None and self.portConfig != None:
            GPIO.setup(self.portNumber, self.portConfig)
            self.isEnabled = True
