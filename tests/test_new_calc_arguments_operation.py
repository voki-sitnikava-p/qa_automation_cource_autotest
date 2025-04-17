from qa_automation_cource.calculator import NewCalc

class TestNewCalcArgumentsOperation:
    def test_new_calc_arguments_operation_positive(self, monkeypatch):
        monkeypatch.setattr(NewCalc, 'number_from_member', lambda: 5)
        first_number, operation, second_number = NewCalc.arguments_operation('4+')
        assert (first_number, operation, second_number) == (4.0, '+', 5), 'Error entering a valid expression'

    def test_new_calc_arguments_operation_negative(self):
        first_number, operation, second_number = NewCalc.arguments_operation(55)
        assert (first_number, operation, second_number) == (None, None, None), 'Invalid input should return Nones'
