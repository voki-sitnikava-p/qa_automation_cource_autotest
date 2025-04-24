import pytest
from qa_automation_cource.calculator import BasicCalc, NewCalc

@pytest.fixture(scope="session")
def calc():
    return BasicCalc()

@pytest.fixture(scope="function")
def new_calc_with_memory(tmp_path, monkeypatch):
    memory_file_path = tmp_path / "memory.txt"
    monkeypatch.setattr("qa_automation_cource.calculator.NewCalc.memory_file", str(memory_file_path))
    calc = NewCalc()
    for i in range(-100, 101, 100):
        calc.memo_plus(i)
    return calc

