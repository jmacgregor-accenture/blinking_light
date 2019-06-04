from blinking_light.blinker import Blinker
from blinking_light.led_light import LedLight
from blinking_light.gpio_port import GpioPort
from blinking_light.colors import Colors
import time
import pytest
import pytest_mock


class TestBlinker:
    @pytest.fixture
    def blinker(self):
        port = GpioPort(5, "OUT")
        blinker = Blinker(port, "blue", 1, 1)
        return blinker

    def test_blinker_blinks_once_per_second_for_ten_seconds(self, blinker):
        blinker.onSeconds = .5
        blinker.offSeconds = .5

        blinker.start(10)

        assert blinker.on_counter == 10

    def test_blinker_blinks_once_with_five_second_intervals_for_ten_seconds(self, blinker):
        blinker.onSeconds = 5
        blinker.offSeconds = 5
        blinker.start(10)

        assert blinker.on_counter == 1

    def test_blinker_light_ends_off_at_end_of_cycle(self, blinker):
        blinker.onSeconds = 5
        blinker.offSeconds = 1

        blinker.start(10)

        assert blinker.on_counter > 0
        assert blinker.isOn == False

    def test_blinker_keepOn_switches_keepBlinking_flag(self, blinker):
        blinker.switchOn()

        assert blinker.keepBlinking == True

    def test_blinker_switchOff_switches_keepBlinking_flag(self, blinker):
        blinker.switchOn()

        blinker.switchOff()

        assert blinker.keepBlinking == False

    def test_blinker_switchOn_calls_startLoop(self, blinker, mocker):
        mocker.spy(blinker, '_startLoop')

        blinker.switchOn()

        assert blinker._startLoop.call_count == 1

    def test_blinker_switchOn_starts_thread(self, blinker):
        blinker.switchOn()

        assert blinker.thread.isAlive() == True

    def test_blinker_switchOff_stops_thread(self, blinker):
        blinker.switchOn()

        blinker.switchOff()

        assert blinker.thread.isAlive() == False

    def test_blinker_has_color(self, blinker):
        
        assert blinker.color == Colors.getColor("blue")

