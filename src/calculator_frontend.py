from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication

from exceptions.invalid_chars_exception import InvalidCharsException
from exceptions.invalid_endwith_exception import InvalidEndwithException
from exceptions.invalid_startwith_exception import InvalidStartwithException
from exceptions.repeated_operators_exception import RepeatedOperatorsException
from src.calculator_backend import CalculatorBackend
from ui.main_window import Ui_MainWindow
from src.validator import Validator


class CalculatorFrontend(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__init_buttons()

        self.validator = Validator()
        
        # self.calc_backend = CalculatorBackend()

        self.show()

    def __input_char(self, char: str | int) -> None:
        line_edit = self.ui.lineEdit_expression
        line_edit.setText(f'{line_edit.text()}{char}')

    def __init_buttons(self):
        for i in range(10):
            btn = self.findChild(QPushButton, f'pushButton_{i}')
            btn.clicked.connect(lambda num=i, *args: self.__input_char(num))

        self.ui.pushButton_devide.clicked.connect(lambda: self.__input_char('/'))
        self.ui.pushButton_multiply.clicked.connect(lambda: self.__input_char('*'))
        self.ui.pushButton_minus.clicked.connect(lambda: self.__input_char('-'))
        self.ui.pushButton_plus.clicked.connect(lambda: self.__input_char('+'))
        self.ui.pushButton_point.clicked.connect(lambda: self.__input_char('.'))
        self.ui.pushButton_percent.clicked.connect(lambda: self.__input_char('%'))

        self.ui.pushButton_eval.clicked.connect(self.__calculate)
        self.ui.pushButton_back.clicked.connect(self.__backspace)
        self.ui.pushButton_c.clicked.connect(self.__clear)

    def __calculate(self) -> None:
        expression = self.ui.lineEdit_expression.text()

        try:
            if not self.validator.validate_chars(expression):
                raise InvalidCharsException(self.validator.invalid_chars)

            if not self.validator.validate_repeated_operators(expression):
                raise RepeatedOperatorsException(self.validator.repeated_operators)

            if not self.validator.validate_startwith(expression):
                raise InvalidStartwithException(self.validator.invalid_startwith)

            if not self.validator.validate_endwith(expression):
                raise InvalidEndwithException(self.validator.invalid_endwith)

            result = CalculatorBackend.calc(expression)
            self.ui.lineEdit_result.setText(str(result))
        except Exception as e:
            self.ui.lineEdit_result.setText(str(e))

    def __backspace(self) -> None:
        expression = self.ui.lineEdit_expression.text()
        self.ui.lineEdit_expression.setText(expression[:-1])

    def __clear(self) -> None:
        self.ui.lineEdit_expression.clear()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() in (Qt.Key_Enter, Qt.Key_Return, Qt.Key_Equal): self.__calculate()
        elif event.key() == Qt.Key_Backspace: self.__backspace()
        elif event.key() == Qt.Key_Period: self.ui.pushButton_point.click()
        elif event.key() == Qt.Key_Asterisk: self.ui.pushButton_multiply.click()
        elif event.key() == Qt.Key_Plus: self.ui.pushButton_plus.click()
        elif event.key() == Qt.Key_Minus: self.ui.pushButton_minus.click()
        elif event.key() == Qt.Key_Slash: self.ui.pushButton_devide.click()
        elif event.key() == Qt.Key_Percent: self.ui.pushButton_percent.click()
        else: super().keyPressEvent(event)



if __name__ == '__main__':
    app = QApplication()
    c = CalculatorFrontend()

    print(c.validator.validate('123'))