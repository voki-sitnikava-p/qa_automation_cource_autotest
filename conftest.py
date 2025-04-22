import pytest
from qa_automation_cource.calculator import BasicCalc, NewCalc

@pytest.fixture(scope="session")
def calc():
    return BasicCalc()

@pytest.fixture(scope="session")
def new_calc():
    return NewCalc()

@pytest.fixture(scope="function")
def new_calc_with_memory():
    calc = NewCalc()
    for i in range(-100, 101, 100):
        calc.memo_plus(i)
    return calc


