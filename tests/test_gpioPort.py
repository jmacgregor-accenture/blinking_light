from blinking_light.gpio_port import GpioPort
from blinking_light.my_fake_rpigio import fake_rpigio as GPIO


def test_gpioPortHasNumber():
    portNum = 18
    port = GpioPort(portNum)

    assert port.portNumber == portNum
