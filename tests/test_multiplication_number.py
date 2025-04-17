import pytest
from random import randint, uniform

from qa_automation_cource.calculator import BasicCalc

class TestMultiplicationNumber:
    @pytest.mark.CRITICAL
    def test_multiplication_positive(self):
        first_number = randint(-100000, 100000)
        second_number = uniform(-20, 20)
        assert BasicCalc.multiplication_number(first_number, '*', second_number) == first_number * second_number, \
            'Sum calculate incorrectly'

    @pytest.mark.CRITICAL
    def test_multiplication_negative(self):
        first_number = 'first'
        second_number = 'second'
        assert BasicCalc.multiplication_number(first_number, '*', second_number) == 0, \
            "Didn't handle incorrect values for arguments"
