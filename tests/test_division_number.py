import pytest
from random import randint, uniform

from qa_automation_cource.calculator import BasicCalc


class TestDivisionNumber:
    @pytest.mark.CRITICAL
    def test_division_positive(self):
        first_number = randint(-100000, 100000)
        second_number = uniform(-20, 20)
        assert BasicCalc.division_number(first_number, '/', second_number) == first_number / second_number, \
            'Sum calculate incorrectly'

    @pytest.mark.CRITICAL
    def test_division_negative(self):
        first_number = 'first'
        second_number = 'second'
        assert BasicCalc.division_number(first_number, '/', second_number) == 0, \
            "Didn't handle incorrect values for arguments"
