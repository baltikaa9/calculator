import pytest
from PySide6.QtWidgets import QApplication

from src.exceptions.invalid_expression import InvalidExpression
from calculator_frontend import CalculatorFrontend

QApplication()
calc = CalculatorFrontend()

class TestCalculatorFrontend:
    @pytest.fixture
    def calculator(self) -> CalculatorFrontend:
        # app = QApplication()
        # yield CalculatorFrontend()
        # del app
        ...

    @pytest.mark.parametrize(
        'symbol',
        [
            ('0'),
            ('1'),
            ('2'),
            ('3'),
            ('4'),
            ('5'),
            ('6'),
            ('7'),
            ('8'),
            ('9'),
        ]
    )
    def test_input_char(self, symbol):
        calc._CalculatorFrontend__input_char(symbol)
        # assert getattr(calc.ui, inp).text() == symbol

        assert getattr(calc.ui, 'lineEdit_expression').text() == symbol
        getattr(calc.ui, 'lineEdit_expression').setText('')

    @pytest.mark.parametrize(
        'btn, text',
        [
            ('pushButton_0','0'),
            ('pushButton_1','1'),
            ('pushButton_2','2'),
            ('pushButton_3','3'),
            ('pushButton_4','4'),
            ('pushButton_5','5'),
            ('pushButton_6','6'),
            ('pushButton_7','7'),
            ('pushButton_8','8'),
            ('pushButton_9','9'),
        ]
    )
    def test_buttons(self, btn, text):
        getattr(calc.ui, btn).click()
        assert getattr(calc.ui, 'lineEdit_expression').text() == text
        getattr(calc.ui, 'lineEdit_expression').setText('')

    def test_clear(self):
        getattr(calc.ui, 'lineEdit_expression').setText('123')
        getattr(calc.ui, 'pushButton_c').click()
        assert getattr(calc.ui, 'lineEdit_expression').text() == ''
