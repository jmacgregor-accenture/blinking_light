from app.setup_circuit import CircuitSetup
from blinking_light.gpio_port import GpioPort
from blinking_light.led_light import LedLight
from blinking_light.blinker import Blinker


class ProgramLoop():

    def __init__(self):
        self.exit = ""
        self.setup = None
        self.blinking = "n"

    def main(self):
        try:
            self.run()
        finally:
            if self.setup.board != None:
                self.setup.board.cleanUp()

    def run(self):
        self.setupCircuit()

        while self.exit != "x":
            if self.blinking == "n":
                self._handleSolidLights()
            else:
                self._handleBlinking()
            self.exit = input("Press 'x' to exit, anything else to turn lights back on: ")

    def _handleSolidLights(self):
        for light in self.setup.lights:
            light.turnOn()
        
        input("Press any key to switch off...")

        for light in self.setup.lights:
            light.turnOff()

    def _handleBlinking(self):
        for light in self.setup.lights:
            light.switchOn()
                
        input("Press any key to stop blinking...")

        for light in self.setup.lights:
            light.switchOff()

    def setupCircuit(self):
        boardConfig = input("What numbering system are you using? (Hit enter to use BCM): ")

        if boardConfig == "":
            boardConfig = "BCM"
        
        self.setup = CircuitSetup(boardConfig)

        numberOfLights = int(input("How many lights are you hooking up? "))

        self.blinking = input("Do your lights blink? (y/n): ")

        if str(self.blinking).lower() == "y":
            self.setupBlinkingLights(numberOfLights)
        else:
            self.setupSolidLeds(numberOfLights)

    def setupBlinkingLights(self, numberOfLights):
        while numberOfLights > 0:
            lightNumber = 1
            portNumber = int(input(str.format("What port is light #{0} connected to? ", lightNumber)))
            color = input("What color is this light? ")
            onTime = int(input("How many seconds should the light be on during each blink? "))
            offTime = int(input("How many seconds should the light be off during each blink? "))

            port = GpioPort(portNumber, "out")
            self.setup.addPort(port)
            light = Blinker(port, color, onTime, offTime)
            self.setup.addLed(light)

            lightNumber += 1
            numberOfLights -= 1

    def setupSolidLeds(self, numberOfLights):
        while numberOfLights > 0:
            portNumber = int(input(str.format("What port is light #{0} connected to? ", numberOfLights)))
            color = input("What color is this light? ")

            port = GpioPort(portNumber, "out")
            self.setup.addPort(port)
            light = LedLight(port, color)
            self.setup.addLed(light)

            numberOfLights -= 1
