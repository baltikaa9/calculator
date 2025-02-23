import pytest
from PySide6.QtWidgets import QApplication

from src.exceptions.invalid_expression import InvalidExpression
from calculator_frontend import CalculatorFrontend

QApplication()
calc = CalculatorFrontend()


class TestCalculator:
    @pytest.fixture
    def calculator(self) -> CalculatorFrontend:
        # app = QApplication()
        # yield CalculatorFrontend()
        # del app
        ...

    @pytest.mark.parametrize(
        'expr, res',
        [
            ('1+1', '2'),
            ('2**2', '4'),
            ('2*(1+5)', '12'),
            ('3/2', '1.5'),
        ]
    )
    def test_calc(self, expr, res):
        calc.ui.lineEdit_expression.setText(expr)
        calc.ui.pushButton_eval.click()
        assert calc.ui.lineEdit_result.text() == res

    @pytest.mark.parametrize(
        'expr, res',
        [
            ('1/0', 'Invalid expression: "1/0". division by zero.'),
            ('1=', 'Неверные символы: (=)'),
            ('1++1', 'Неверные операторы: (++)'),
            ('*1', 'Выражение не должно начинаться с *'),
            ('1-', 'Выражение не должно заканчиваться на -'),
        ]
    )
    def test_invalid_expr(self, expr, res):
        calc.ui.lineEdit_expression.setText(expr)
        calc.ui.pushButton_eval.click()
        assert calc.ui.lineEdit_result.text() == res
