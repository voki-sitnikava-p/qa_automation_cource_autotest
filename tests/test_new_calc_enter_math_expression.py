from qa_automation_cource.calculator import NewCalc

class TestNewCalcEnterMathExpression:
    def test_new_calc_enter_math_expression_positive(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '33-')
        result = NewCalc.enter_math_expression()
        assert result == '33-', 'Error entering a valid expression'


    def test_new_calc_enter_math_expression_negative(self, monkeypatch):
        enter = iter(['dff', '+3', '44-4', '55+'])
        monkeypatch.setattr('builtins.input', lambda _: next(enter))
        result = NewCalc.enter_math_expression()
        assert result == '55+', 'Error when entering an invalid expression'
