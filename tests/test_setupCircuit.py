from app.setup_circuit import CircuitSetup
from blinking_light.my_fake_rpigio import fake_rpigio as GPIO
from blinking_light.gpio_port import GpioPort
import pytest

class TestCircuitSetup():

    @pytest.fixture
    def circuitSetup(self):
        setup = CircuitSetup("BCM")
        return setup

    def test_circuitSetup_has_board(self, circuitSetup):
        
        assert circuitSetup.board.config == GPIO.BCM

    def test_circuitSetup_can_add_ports(self, circuitSetup):
        port = GpioPort(18, "out")
        circuitSetup.addPort(port)

        assert len(circuitSetup.board.ports) == 1
