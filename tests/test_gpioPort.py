from blinking_light.gpio_port import GpioPort
from blinking_light.my_fake_rpigio import fake_rpigio as GPIO
import pytest


class TestGpioPort():

    @pytest.fixture
    def port(self):
        portNum = 18
        portConfig = "out"
        return GpioPort(portNum, portConfig)

    def test_gpioPortHasNumber(self, port):
        expectedPortConfig = GPIO.OUT

        assert port.portNumber == 18
        assert port.portConfig == expectedPortConfig
        assert port.isEnabled == True

    def test_gpioPortCanTurnOnPower(self, port):
        port.powerOn()

        assert port.isPowered == True

    def test_gpioPortDoesNotPowerIfConfigIsBad(self):
        portNum = 18
        portConfig = "purple"
        port = GpioPort(portNum, portConfig)

        port.powerOn()

        assert port.isPowered == False

    def test_gpioPortPowersOff(self, port):
        port.powerOn()

        assert port.isPowered == True

        port.powerOff()

        assert port.isPowered == False

    def test_gpioPortCleansUp(self, port):
        port.powerOn()

        assert port.isPowered == True

        port.cleanUp()

        assert port.isPowered == False
        assert port.isEnabled == False
