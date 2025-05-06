import ast
from qa_automation_cource.calculator import BasicCalc

class TestLogInformation:
    def test_log_information_positive(self, tmp_path):
        BasicCalc.log_file_path = tmp_path / "log.txt"
        BasicCalc.log_information(30, '-', 10, 20)
        with open(BasicCalc.log_file_path, 'r') as file:
            log = ast.literal_eval(file.read())
        assert (log['first_argument'] == 30 and
                log['operation'] == '-' and
                log['second_argument'] == 10 and
                log['result'] == 20), 'Data written to log incorrectly'

    def test_log_information_negative(self, tmp_path):
        BasicCalc.log_file_path = tmp_path / "log.txt"
        BasicCalc.log_information(10, '/', 0, None)
        with open(BasicCalc.log_file_path, 'r') as file:
            log = ast.literal_eval(file.read())
        assert (log['first_argument'] == 10 and
                log['operation'] == '/' and
                log['second_argument'] == 0 and
                log['result'] is None), 'Data written to log incorrectly'
