from qa_automation_cource.calculator import BasicCalc

class TestBasicCalcArgumentsOperation:
    def test_basic_calc_arguments_operation_positive(self):
        first_number, operation, second_number = BasicCalc.arguments_operation('4+55.5')
        assert (first_number, operation, second_number) == (4.0, '+', 55.5), 'Error entering a valid expression'

    def test_basic_calc_arguments_operation_negative(self):
        first_number, operation, second_number = BasicCalc.arguments_operation(55)
        assert (first_number, operation, second_number) == (None, None, None), 'Invalid input should return Nones'
