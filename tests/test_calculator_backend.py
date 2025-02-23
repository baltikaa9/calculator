import pytest

from src.exceptions.invalid_expression import InvalidExpression
from calculator_backend import CalculatorBackend


class TestCalculatorBackend:
    @pytest.mark.parametrize(
        'expression, expected',
        [
            ('1+1', 2),
            ('123+456', 579),
            ('10-5*2', 0),
            ('(3+5)/2', 4),
            ('2**3', 8),
            ('10//3', 3),
            ('-42+18', -24),
            ('0.5+1.25', 1.75),
            ('3*(4+2)', 18),
        ]
    )
    def test_calc(self, expression, expected) -> None:
        assert CalculatorBackend.calc(expression) == expected

    def test_division_by_zero(self) -> None:
        with pytest.raises(InvalidExpression) as e:
            CalculatorBackend.calc('1/0')

        assert str(e.value) == 'Invalid expression: "1/0". division by zero.'
