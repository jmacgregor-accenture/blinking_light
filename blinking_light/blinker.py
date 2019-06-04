from blinking_light import __devenv__
from blinking_light.led_light import LedLight
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

    def keepOn(self):
        self.keepBlinking = True
