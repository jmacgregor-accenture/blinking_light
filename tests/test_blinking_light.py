from blinking_light import __version__
from blinking_light.circuit_controller import CircuitController

def test_version():
    assert __version__ == '0.1.0'

def test_controllerClassExists():
    controller = CircuitController()

    assert controller is not None
