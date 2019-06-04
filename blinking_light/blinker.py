from blinking_light import __devenv__
from blinking_light.led_light import LedLight
import threading
if __devenv__:
    from blinking_light.my_fake_rpigio import fake_rpigio as GPIO
else:
    import RPi.GPIO as GPIO


class Blinker(LedLight):
    
    def start(self, on_seconds, off_seconds, total_duration):
        run_duration = 0
        self.on_counter = 0

        while run_duration < total_duration:
            self.turnOn()
            self.turnOff()
            run_duration += on_seconds+off_seconds

    def switchOn(self):
        self.keepBlinking = True
        self.thread = threading.Thread(target=self._startLoop, args=())
        self.thread.daemon = True
        self.thread.start()


    def switchOff(self):
        self.keepBlinking = False

    def _startLoop(self):
        pass