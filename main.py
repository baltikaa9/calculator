import sys

from PySide6.QtWidgets import QApplication

from src.calculator_frontend import CalculatorFrontend

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorFrontend()

    app.exec()
