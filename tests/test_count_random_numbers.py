import pytest


class TestCountRandomNumbers:
    def test_count_random_numbers_positive(self, calc, capsys):
        calc.count_random_numbers()
        captured = capsys.readouterr()
        output = captured.out
        assert 'число' in output, "Doesn't display text"

    def test_count_random_numbers_negative(self, calc, monkeypatch):
        def broken_randint(a, b):
            raise ValueError('Random number generation error')
        monkeypatch.setattr('qa_automation_cource.calculator.randint', broken_randint)
        with pytest.raises(ValueError, match='Random number generation error'):
            calc.count_random_numbers()
