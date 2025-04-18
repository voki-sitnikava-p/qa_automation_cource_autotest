import pytest
from math import factorial
from random import randint

from qa_automation_cource.calculator import BasicCalc


class TestFactorial:
    def test_factorial_positive(self):
        f_for_calc = randint(1, 1000)
        factorial_calc = BasicCalc.factorial(f_for_calc)
        assert factorial_calc == factorial(f_for_calc), 'Error positiv factorial'

    def test_factorial_negative(self):
        with pytest.raises(ValueError, match = "Number must be positive"):
            BasicCalc.factorial(-100)
