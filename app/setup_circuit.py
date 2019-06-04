from blinking_light.gpio_board import GpioBoard

class CircuitSetup():

    def __init__(self, boardConfig):
        self.board = GpioBoard(boardConfig)

    def addPort(self, port):
        self.board.addPort(port)