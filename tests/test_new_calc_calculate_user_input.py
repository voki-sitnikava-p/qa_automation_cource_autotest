from qa_automation_cource.calculator import NewCalc

class TestNewCalcCalculateUserInput:
    def test_new_calc_calculate_user_input_positive(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '4+')
        monkeypatch.setattr(NewCalc, 'number_from_member', lambda: 5)
        result = NewCalc.calculate_user_input()
        assert result == 9, 'Error entering a valid expression'

    def test_new_calc_calculate_user_input_negative(self, monkeypatch):
        enter = iter(['5%10', '', '55+'])
        monkeypatch.setattr('builtins.input', lambda _: next(enter))
        monkeypatch.setattr(NewCalc, 'number_from_member', lambda: 0)
        result = NewCalc.calculate_user_input()
        assert result == 55, 'Error when entering an invalid expression'
