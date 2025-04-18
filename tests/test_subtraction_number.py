import pytest
from random import randint, uniform

from qa_automation_cource.calculator import BasicCalc


class TestSubtractionNumber:
    @pytest.mark.xfail(reason='Баг в функции subtraction_number (вместо вычитания сложение)')
    @pytest.mark.CRITICAL
    def test_subtraction_positive(self):
        first_number = randint(-100000, 100000)
        second_number = uniform(-20, 20)
        assert BasicCalc.subtraction_number(first_number, '-', second_number) == first_number - second_number, \
            'Sum calculate incorrectly'

    @pytest.mark.CRITICAL
    def test_subtraction_negative(self):
        first_number = ''
        second_number = [1, 2]
        assert BasicCalc.subtraction_number(first_number, '-', second_number) == 0, \
            "Didn't handle incorrect values for arguments"
