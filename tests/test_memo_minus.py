import pytest
from qa_automation_cource.calculator import NewCalc

class TestMemoMinus:
    def test_memo_minus_positive(self):
        stack = [3, 4, 5]
        delet_value = NewCalc.memo_minus(stack)
        assert stack == [3, 4], 'Removes the wrong value'

    def test_memo_minus_negative(self, tmp_path, monkeypatch):
        with pytest.raises(IndexError, match='pop from empty list'):
            NewCalc.memo_minus([])
