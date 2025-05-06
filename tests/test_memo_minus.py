import pytest
from qa_automation_cource.calculator import NewCalc

class TestMemoMinus:
    def test_memo_minus_positive(self, new_calc_with_memory):
        stack = new_calc_with_memory.memory()
        delet_value = new_calc_with_memory.memo_minus(stack)
        assert stack == ['-100', '0'], 'Removes the wrong value'

    def test_memo_minus_negative(self, tmp_path):
        with pytest.raises(IndexError, match='pop from empty list'):
            NewCalc.memo_minus([])
