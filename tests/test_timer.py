import time
import pytest
from qa_automation_cource.calculator import timer, BasicCalc


class TestTimer:
    def test_timer_positive(self):
        start = time.time()
        with timer():
            time.sleep(0.3)
        end = time.time()
        assert 0.4 >= end - start >= 0.3, "The timer counts the time incorrectly"

    def test_timer_negative(self, capsys):
        with pytest.raises(ValueError, match = "Number must be positive"):
            with timer():
                BasicCalc.factorial(-100)
        captured = capsys.readouterr()
        assert "Время выполнения:" in captured.out
