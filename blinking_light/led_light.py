from blinking_light.colors import Colors

class LedLight():

    def __init__(self, port, color):
        self.port = port
        self.color = Colors.getColor(color)
        self.isOn = False
        self.on_counter = 0

    def turnOn(self):
        self.port.powerOn()
        self.isOn = True
        self.on_counter += 1

    def turnOff(self):
        self.port.powerOff()
        self.isOn = False
