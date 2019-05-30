from blinking_light.gpio_port import GpioPort
from blinking_light.led_light import LedLight
import pytest


class TestLedLight:

    @pytest.fixture
    def light(self):
        port = GpioPort(7, "OUT")
        return LedLight(port)

    def test_ledLightHasGpioBoard(self, light):
        assert isinstance(light.port, GpioPort)

    def test_canTurnOn(self, light):
        light.turnOn()

        assert light.isOn == True

    def test_canTurnOff(self, light):
        light.turnOn()

        light.turnOff()

        assert light.isOn == False
