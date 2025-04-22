import pytest
from random import randint, uniform

from qa_automation_cource.calculator import BasicCalc

@pytest.fixture
def data_parametrize(request):
    request.cls.data = [(-5, 10, -50), (100, 0, 0), (11.5, 11, 126.5), (0, 0, 0), ('string', 'another', 0)]


@pytest.mark.usefixtures('data_parametrize')
class TestMultiplicationNumber:
    @pytest.mark.CRITICAL
    def test_multiplication_positive(self):
        data = self.data
        for arg in data:
            assert BasicCalc.multiplication_number(arg[0], '*', arg[1]) == arg[2], \
            'incorrectly result'

    @pytest.mark.CRITICAL
    def test_multiplication_negative(self):
        first_number = None
        second_number = {1:2}
        assert BasicCalc.multiplication_number(first_number, '*', second_number) == 0, \
            "Didn't handle incorrect values for arguments"
