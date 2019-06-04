from app.setup_circuit import CircuitSetup
from blinking_light.my_fake_rpigio import fake_rpigio as GPIO
from blinking_light.gpio_port import GpioPort
from blinking_light.led_light import LedLight
import pytest

class TestCircuitSetup():

    @pytest.fixture
    def circuitSetup(self):
        return CircuitSetup("BCM")
    
    @pytest.fixture
    def newPort(self):
        return GpioPort(18, "out")

    def test_circuitSetup_has_board(self, circuitSetup):
        
        assert circuitSetup.board.config == GPIO.BCM

    def test_circuitSetup_can_add_ports(self, circuitSetup, newPort):
        circuitSetup.addPort(newPort)

        assert len(circuitSetup.board.ports) == 1

    def test_circuitSetup_can_add_lights(self, circuitSetup, newPort):
        circuitSetup.addPort(newPort)
        led = LedLight(newPort, "red")

        circuitSetup.addLed(led)

        assert len(circuitSetup.lights) == 1
