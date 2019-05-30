from blinking_light.gpio_port import GpioPort
from blinking_light.led_light import LedLight

def test_ledLightHasGpioBoard():
    port = GpioPort(7, "OUT")
    light = LedLight(port)

    assert isinstance(light.port, GpioPort)

def test_canTurnOn():
    port = GpioPort(7, "OUT")
    light = LedLight(port)

    light.turnOn()

    assert light.isOn == True

def test_canTurnOff():
    port = GpioPort(7, "OUT")
    light = LedLight(port)
    light.turnOn()

    light.turnOff()

    assert light.isOn == False