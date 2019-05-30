from blinking_light.gpio_board import GpioBoard
from blinking_light.gpio_port import GpioPort
from blinking_light.my_fake_rpigio import fake_rpigio as GPIO


def createBoard():
    board = GpioBoard("BCM")
    return board

def test_gpioBoardHasBoardConfiguration():
    config = "BCM"
    board = GpioBoard(config)

    assert board.config == GPIO.BCM

def test_gpioBoardHasPorts():
    board = createBoard()
    port = GpioPort(22, "out")

    board.addPort(port)

    assert len(board.ports) == 1
    assert board.ports[0] == port

def test_gpioBoardCanCleanUp():
    board = createBoard()

    board.cleanUp()

    assert board.config == None

def test_gpioBoardCleansUpPorts():
    board = createBoard()
    port = GpioPort(18, "out")
    assert port.isEnabled is True
    board.addPort(port)

    loadedPort = board.ports[1]
    assert loadedPort.portNumber is 18
    assert loadedPort.isEnabled is True

    board.cleanUp()

    assert board.ports[0].isEnabled == False
