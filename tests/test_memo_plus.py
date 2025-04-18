from qa_automation_cource.calculator import NewCalc

class TestMemoPlus:
    def test_memo_plus_positive(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        NewCalc.memo_plus(20)
        stack = NewCalc.memory()
        assert int(stack[-1]) == 20, 'The result is not written to memory'

    def test_memo_plus_negative(self, tmp_path, monkeypatch, capsys):
        monkeypatch.chdir(tmp_path)
        NewCalc.memo_plus('test')
        captured = capsys.readouterr()
        output = captured.out
        assert 'The result cannot be written to file. Result must be a number.' in output, 'Error transmitting invalid data'
