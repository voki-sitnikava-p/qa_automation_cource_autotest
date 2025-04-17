from qa_automation_cource.calculator import NewCalc

class TestMemory:
    def test_memory_positive(self):
        res_memory = NewCalc.memory()
        assert isinstance(res_memory, list), 'Invalid type of returned argument'

    def test_memory_negative(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        result = NewCalc.memory()
        assert result == [], 'Returned not empty list'
