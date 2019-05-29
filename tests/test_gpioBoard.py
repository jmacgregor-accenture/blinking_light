from blinking_light.gpio_board import GpioBoard
from blinking_light.my_fake_rpigio import fake_rpigio as GPIO


def createBoardAndEnablePort():
    board = GpioBoard("BCM")
    board.enablePort(18, "OUT")
    return board

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
    board = createBoardAndEnablePort()

    board.powerOn()

    assert board.portPowered == True

def test_gpioBoardCanShutOffPowerToPort():
    board = createBoardAndEnablePort()

    board.powerOn()
    board.powerOff()

    assert board.portPowered == False

def test_gpioBoardCanCleanUp():
    board = createBoardAndEnablePort()
    board.powerOn()

    board.cleanUp()

    assert board.portEnabled == False
    assert board.portPowered == False
    assert board.boardMode == None
    assert board.portMode == None