import pytest

from src.exceptions.invalid_expression import InvalidExpression
from src.exceptions.invalid_chars_exception import InvalidCharsException
from src.exceptions.invalid_endwith_exception import InvalidEndwithException
from src.exceptions.invalid_startwith_exception import InvalidStartwithException
from src.exceptions.repeated_operators_exception import RepeatedOperatorsException
from src.calculator_backend import CalculatorBackend
from src.validator import Validator


class TestCalculatorBackend:
    @pytest.fixture
    def validator(self) -> Validator:
        return Validator()

    def test_normal(self, validator: Validator) -> None:
        expr = '1+1'
        is_valid = validator.validate(expr)
        res = CalculatorBackend.calc('1+1')
        assert is_valid is True
        assert res == 2

    def test_invalid_chars(self, validator: Validator) -> None:
        expr = '1+a'
        is_valid = validator.validate_chars(expr)

        with pytest.raises(InvalidExpression) as e:
            CalculatorBackend.calc('1+a')

        assert is_valid is False
        assert validator.invalid_chars == ['a']
        # assert str(e.value) == 'Неверные символы: (a)'
        # assert e.value.chars == ['a']

    def test_invalid_operators(self, validator: Validator) -> None:
        expr = '1++1'
        is_valid = validator.validate_repeated_operators(expr)
        assert is_valid is False
        assert validator.repeated_operators == ['++']

        res = CalculatorBackend.calc('1++1')

        assert res == 2

        # assert str(e.value) == 'Неверные операторы: (++)'
        # assert e.value.chars == ['++']

    def test_normal_startwith(self, validator: Validator) -> None:
        expr = '-1'
        is_valid = validator.validate_startwith(expr)
        assert is_valid is True
        assert validator.invalid_startwith is None

        res = CalculatorBackend.calc('-1')
        assert res == -1

    def test_invalid_startwith(self, validator: Validator) -> None:
        expr = '*1'
        is_valid = validator.validate_startwith(expr)
        assert is_valid is False
        assert validator.invalid_startwith == ['*']

        with pytest.raises(InvalidExpression) as e:
            CalculatorBackend.calc('*1')

        # assert str(e.value) == 'Выражение не должно начинаться с *'
        # assert e.value.chars == ['*']

    def test_invalid_endwith(self, validator: Validator) -> None:
        expr = '1+'
        is_valid = validator.validate_endwith(expr)
        assert is_valid is False
        assert validator.invalid_endwith == ['+']

        with pytest.raises(InvalidExpression) as e:
            CalculatorBackend.calc('1+')

        # assert str(e.value) == 'Выражение не должно заканчиваться на +'
        # assert e.value.chars == ['+']
