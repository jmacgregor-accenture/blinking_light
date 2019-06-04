from blinking_light.gpio_board import GpioBoard

class CircuitSetup():

    def __init__(self, boardConfig):
        self.board = GpioBoard(boardConfig)
        self.lights = []

    def addPort(self, port):
        self.board.addPort(port)

    def addLed(self, led):
        self.lights.append(led)
    