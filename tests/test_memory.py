from qa_automation_cource.calculator import NewCalc

class TestMemory:
    def test_memory_positive(self, new_calc_with_memory):
        res_memory = new_calc_with_memory.memory()
        assert res_memory == ['-100', '0', '100'], 'Returned invalid result'

    def test_memory_negative(self, tmp_path, monkeypatch):
        memory_file = tmp_path / "memory.txt"
        monkeypatch.setattr(NewCalc, "memory_file", str(memory_file))
        result = NewCalc.memory()
        assert result == [], 'Returned not empty list'
