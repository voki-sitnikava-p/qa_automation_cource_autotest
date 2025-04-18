from qa_automation_cource.calculator import BasicCalc

class TestBasicCalcEnterMathExpression:
    def test_basic_calc_enter_math_expression_positive(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '4+5')
        result = BasicCalc.enter_math_expression()
        assert result == '4+5', 'Error entering a valid expression'


    def test_basic_calc_enter_math_expression_negative(self, monkeypatch):
        enter = iter(['dff', '12-+3', '5*22'])
        monkeypatch.setattr('builtins.input', lambda _: next(enter))
        result = BasicCalc.enter_math_expression()
        assert result == '5*22', 'Error when entering an invalid expression'
