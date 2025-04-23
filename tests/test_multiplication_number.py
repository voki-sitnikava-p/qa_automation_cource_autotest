import pytest
from random import randint, uniform

from qa_automation_cource.calculator import BasicCalc

@pytest.fixture(params=[
    (-5, 10, -50),
    (100, 0, 0),
    (11.5, 11, 126.5),
    (0, 0, 0),
    ('string', 'another', 0)
])
def data_parametrize(request):
    return request.param

class TestMultiplicationNumber:
    @pytest.mark.CRITICAL
    def test_multiplication_positive(self, data_parametrize):
        first_number, second_number, result = data_parametrize
        assert BasicCalc.multiplication_number(first_number, '*', second_number) == result, \
            f'error in {first_number} * {second_number} = {result}'


    @pytest.mark.CRITICAL
    def test_multiplication_negative(self):
        first_number = None
        second_number = {1:2}
        assert BasicCalc.multiplication_number(first_number, '*', second_number) == 0, \
            "Didn't handle incorrect values for arguments"
