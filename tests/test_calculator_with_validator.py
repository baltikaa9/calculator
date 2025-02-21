import pytest

from exceptions.invalid_chars_exception import InvalidCharsException
from exceptions.invalid_endwith_exception import InvalidEndwithException
from exceptions.invalid_startwith_exception import InvalidStartwithException
from exceptions.repeated_operators_exception import RepeatedOperatorsException
from calculator_backend import CalculatorBackend
from validator import Validator


class TestCalculatorBackend:
    @pytest.fixture
    def calculator(self) -> CalculatorBackend:
        return CalculatorBackend(Validator())

    def test_normal(self, calculator: CalculatorBackend) -> None:
        res = calculator.calc('1+1')
        assert res == 2

    def test_invalid_chars(self, calculator: CalculatorBackend) -> None:
        with pytest.raises(InvalidCharsException) as e:
            calculator.calc('1+a')

        assert str(e.value) == 'Неверные символы: (a)'
        assert e.value.chars == ['a']

    def test_invalid_operators(self, calculator: CalculatorBackend) -> None:
        with pytest.raises(RepeatedOperatorsException) as e:
            calculator.calc('1++1')

        assert str(e.value) == 'Неверные операторы: (++)'
        assert e.value.chars == ['++']

    def test_normal_startwith(self, calculator: CalculatorBackend) -> None:
        res = calculator.calc('-1')
        assert res == -1

    def test_invalid_startwith(self, calculator: CalculatorBackend) -> None:
        with pytest.raises(InvalidStartwithException) as e:
            calculator.calc('*1')

        assert str(e.value) == 'Выражение не должно начинаться с *'
        assert e.value.chars == ['*']

    def test_invalid_endwith(self, calculator: CalculatorBackend) -> None:
        with pytest.raises(InvalidEndwithException) as e:
            calculator.calc('1+')

        assert str(e.value) == 'Выражение не должно заканчиваться на +'
        assert e.value.chars == ['+']
