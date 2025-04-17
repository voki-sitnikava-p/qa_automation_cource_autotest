import pytest
from random import randint, uniform

from qa_automation_cource.calculator import BasicCalc


class TestSumNumber:
    @pytest.mark.parametrize('first_number, second_number, result', [
        ([1, 10, 100, -10, 11.5, 0], None, sum([1, 10, 100, -10, 11.5, 0])),
        ([40], None, 40),
        ([], None, 0),
        ((-1, 2, 3, 0), None, 4),
        ({-5, 10, 0}, None, 5),
        (5, 1000, 5 + 1000),
        (-100, 1, -100 + 1),
        (5.6, 11, 5.6 + 11),
        (0, 0, 0),
        ('string', 'another', 0)
    ], ids=['sum list', 'sum list with 1 element', 'sum empty list',
            'sum tuple', 'sum set', 'sum positive integer', 'positive + negative',
            'integer + non-integer', 'sum zero', 'invalid strings'])

    def test_sum_parametrize(self, first_number, second_number, result):
        '''
        Параметрезированный тест для функции sum_number.
        Я выбрала эту функцию т.к. она является основной функцией калькулятора,
        обрабатывает некорректные значения, суммирует числа
        а так же может принимать итерируемый объект и выводить его сумму.
        '''
        assert result == BasicCalc.sum_number(first_number, '+', second_number), 'Sum calculate incorrectly'

    @pytest.mark.CRITICAL
    def test_sum_positive(self):
        first_number = randint(-100000, 100000)
        second_number = uniform(-20, 20)
        assert BasicCalc.sum_number(first_number, '+', second_number) == first_number + second_number, \
            'Sum calculate incorrectly'

    @pytest.mark.CRITICAL
    def test_sum_negative(self):
        first_number = 'first'
        second_number = 'second'
        assert BasicCalc.sum_number(first_number, '+', second_number) == 0, \
            "Didn't handle incorrect values for arguments"
