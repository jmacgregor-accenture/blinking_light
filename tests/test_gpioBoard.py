from blinking_light.gpio_board import GpioBoard
from blinking_light.my_fake_rpigio import fake_rpigio as GPIO

def test_gpioBoardHasBoardMode():
    mode = "BCM"
    board = GpioBoard(mode)

    assert board.boardMode == GPIO.BCM

def test_gpioBoardCanEnablePort():
    boardMode = GPIO.BCM
    port = 18
    mode = "OUT"
    board = GpioBoard(boardMode)

    board.enablePort(port, mode)

    assert board.portEnabled == True
    assert board.portMode == GPIO.OUT
    assert board.portNumber == port

def test_gpioBoardCanSendPowerToPort():
    boardMode = GPIO.BCM
    port = 18
    mode = "OUT"
    board = GpioBoard(boardMode)
    board.enablePort(port, mode)

    board.powerOn()

    assert board.portPowered == True