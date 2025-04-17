import pytest

from qa_automation_cource.calculator import initialization_cache, BasicCalc

class TestInitializationCache:
    def test_initialization_cache_positive(self, capsys):
        for i in initialization_cache(10):
            pass
        captured = capsys.readouterr()
        assert 'Инициализация изначальных значений для кэша факториалов завершена' in captured.out

    def test_initialization_cache_negative(self):
        with pytest.raises(ValueError, match="Number must be positive"):
            for i in initialization_cache(-10):
                pass
