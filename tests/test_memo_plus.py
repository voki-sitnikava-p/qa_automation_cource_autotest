from qa_automation_cource.calculator import NewCalc

class TestMemoPlus:
    def test_memo_plus_positive(self, new_calc_with_memory, monkeypatch):
        new_calc_with_memory.memo_plus(20)
        stack = new_calc_with_memory.memory()
        assert int(stack[-1]) == 20, 'The result is not written to memory'

    def test_memo_plus_negative(self, new_calc_with_memory, monkeypatch, capsys):
        new_calc_with_memory.memo_plus('test')
        captured = capsys.readouterr()
        output = captured.out
        assert 'The result cannot be written to file. Result must be a number.' in output, 'Error transmitting invalid data'
