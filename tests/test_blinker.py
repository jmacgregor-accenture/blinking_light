from blinking_light.blinker import Blinker
from blinking_light.led_light import LedLight
from blinking_light.gpio_port import GpioPort
import time
import pytest


class TestBlinker:
    @pytest.fixture
    def blinker(self):
        port = GpioPort(5, "OUT")
        blinker = Blinker(port)
        return blinker

    def test_blinker_blinks_once_per_second_for_ten_seconds(self, blinker):

        blinker.start(.5, .5, 10)

        assert blinker.on_counter == 10

    def test_blinker_blinks_once_with_five_second_intervals_for_ten_seconds(self, blinker):

        blinker.start(5, 5, 10)

        assert blinker.on_counter == 1

    def test_blinker_light_ends_off_at_end_of_cycle(self, blinker):
        blinker.start(5, 1, 10)

        assert blinker.on_counter > 0
        assert blinker.isOn == False
