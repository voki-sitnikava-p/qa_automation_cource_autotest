import pytest
from qa_automation_cource.calculator import BasicCalc


class TestCountRandomNumbers:
    def test_count_random_numbers_positive(self, capsys):
        calc = BasicCalc()
        calc.count_random_numbers()
        captured = capsys.readouterr()
        output = captured.out
        assert 'число' in output, "Doesn't display text"

    def test_count_random_numbers_negative(self, monkeypatch):
        def broken_randint(a, b):
            raise ValueError('Random number generation error')
        monkeypatch.setattr('qa_automation_cource.calculator.randint', broken_randint)
        calc = BasicCalc()
        with pytest.raises(ValueError, match='Random number generation error'):
            calc.count_random_numbers()
