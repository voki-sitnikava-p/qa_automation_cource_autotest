from qa_automation_cource.calculator import BasicCalc

class TestBasicCalcCalculateUserInput:
    def test_basic_calc_calculate_user_input_positive(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '4+5')
        result = BasicCalc.calculate_user_input()
        assert result == 9, 'Error entering a valid expression'

    def test_basic_calc_calculate_user_input_negative(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '4/0')
        result = BasicCalc.calculate_user_input()
        assert result is None, 'No error when dividing by 0'
