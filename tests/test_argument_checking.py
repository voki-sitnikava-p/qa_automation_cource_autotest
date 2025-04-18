from qa_automation_cource.calculator import BasicCalc

class TestArgumentChecking:
    def test_argument_check_positive(self):
        first_number = -10.3
        second_number = 1000
        first_check, second_check = BasicCalc.argument_checking(first_number, second_number, '-')
        assert first_check == first_number and second_check == second_number, 'Error checking for correct argument'

    def test_argument_check_negative(self):
        first_number = 'first'
        second_number = 'second'
        first_check, second_check = BasicCalc.argument_checking(first_number, second_number, '-')
        assert first_check == 0 and second_check == 0, 'Error checking for incorrect argument'
