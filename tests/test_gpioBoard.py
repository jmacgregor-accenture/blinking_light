from blinking_light.gpio_board import GpioBoard

def test_gpioBoardHasPortAndMode():
    port = 18
    mode = "OUT"
    board = GpioBoard(port, mode)

    assert board.portNumber == port
    assert board.mode == mode