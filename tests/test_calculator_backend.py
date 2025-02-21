import pytest

from exceptions.invalid_expression import InvalidExpression
from calculator_backend import CalculatorBackend


class TestCalculatorBackend:
    @pytest.fixture
    def calculator(self) -> CalculatorBackend:
        return CalculatorBackend()

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
    def test_calc(self, calculator: CalculatorBackend, expression, expected) -> None:
        assert calculator.calc(expression) == expected

    def test_division_by_zero(self, calculator: CalculatorBackend) -> None:
        with pytest.raises(InvalidExpression) as e:
            calculator.calc('1/0')

        assert str(e.value) == 'Invalid expression: "1/0". division by zero.'
