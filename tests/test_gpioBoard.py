from blinking_light.gpio_board import GpioBoard
from blinking_light.my_fake_rpigio import fake_rpigio as GPIO


def createBoard():
    board = GpioBoard("BCM")
    return board

def test_gpioBoardHasBoardConfiguration():
    config = "BCM"
    board = GpioBoard(config)

    assert board.config == GPIO.BCM

def test_gpioBoardCanCleanUp():
    board = createBoard()

    board.cleanUp()

    assert board.boardMode == None
