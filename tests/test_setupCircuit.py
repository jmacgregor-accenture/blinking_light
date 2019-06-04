from app.setup_circuit import CircuitSetup
from blinking_light.my_fake_rpigio import fake_rpigio as GPIO
import pytest

class TestCircuitSetup():

    @pytest.fixture
    def circuitSetup(self):
        setup = CircuitSetup("BCM")
        return setup

    def test_circuitSetup_has_board(self, circuitSetup, mocker):
        
        assert circuitSetup.board.config == GPIO.BCM
