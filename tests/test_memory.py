from qa_automation_cource.calculator import NewCalc

class TestMemory:
    def test_memory_positive(self, new_calc_with_memory):
        res_memory = new_calc_with_memory.memory()
        assert res_memory == ['-100', '0', '100'], 'Returned invalid result'

    def test_memory_negative(self, new_calc_with_memory, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        result = new_calc_with_memory.memory()
        assert result == [], 'Returned not empty list'
