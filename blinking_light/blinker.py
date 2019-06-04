from blinking_light import __devenv__
from blinking_light.led_light import LedLight
from blinking_light.colors import Colors
import threading
import time
if __devenv__:
    from blinking_light.my_fake_rpigio import fake_rpigio as GPIO
else:
    import RPi.GPIO as GPIO


class Blinker(LedLight):
    
    def __init__(self, port, color, on_seconds, off_seconds):
        self.onSeconds = on_seconds
        self.offSeconds = off_seconds
        super().__init__(port, color)

    def start(self, total_duration):
        run_duration = 0
        self.on_counter = 0

        while run_duration < total_duration:
            self._blink()
            run_duration += self.onSeconds + self.offSeconds

    def switchOn(self):
        self.keepBlinking = True
        self.thread = threading.Thread(target=self._startLoop, args=())
        self.thread.daemon = True
        self.thread.start()

    def switchOff(self):
        self.keepBlinking = False
        self.thread.join()

    def _startLoop(self):
        while self.keepBlinking == True:
            self._blink()

    def _blink(self):
        self.turnOn()
        time.sleep(self.onSeconds)
        self.turnOff()
        time.sleep(self.offSeconds)
