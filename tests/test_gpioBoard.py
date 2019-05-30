from blinking_light.gpio_board import GpioBoard
from blinking_light.gpio_port import GpioPort
from blinking_light.my_fake_rpigio import fake_rpigio as GPIO
import pytest


class TestGpioBoard():

    @pytest.fixture
    def board(self):
        return GpioBoard("BCM")

    def test_gpioBoardHasBoardConfiguration(self, board):
        assert board.config == GPIO.BCM

    def test_gpioBoardHasPorts(self, board):
        port = GpioPort(22, "out")

        board.addPort(port)

        assert len(board.ports) == 1
        assert board.ports[0] == port

    def test_gpioBoardCanCleanUp(self, board):
        board.cleanUp()

        assert board.config == None

    def test_gpioBoardCleansUpPorts(self, board):
        port = GpioPort(18, "out")
        board.addPort(port)

        loadedPort = board.ports[0]
        assert loadedPort.portNumber is 18
        assert loadedPort.isEnabled is True

        board.cleanUp()

        assert board.ports[0].isEnabled == False
