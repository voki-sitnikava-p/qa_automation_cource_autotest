import pytest
from qa_automation_cource.calculator import NewCalc

class TestNumberFromMember:
    def test_number_from_member_positive(self, monkeypatch):
        monkeypatch.setattr(NewCalc, 'memory', lambda: [])
        number = NewCalc.number_from_member()
        assert number == 0, "Doesn't return 0 if there are no numbers in memory"

    def test_number_from_member_negative(self, tmp_path, monkeypatch):
        monkeypatch.setattr(NewCalc, 'memory', lambda: ['test'])
        with pytest.raises(ValueError,  match="could not convert string to float: 'test'"):
            float(NewCalc.number_from_member())
