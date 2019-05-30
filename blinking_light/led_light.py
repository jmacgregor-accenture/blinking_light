class LedLight():

    def __init__(self, port):
        self.port = port

    def turnOn(self):
        self.port.powerOn()
        self.isOn = True