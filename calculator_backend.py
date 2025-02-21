from exceptions.invalid_chars_exception import InvalidCharsException
from exceptions.invalid_expression import InvalidExpression
from validator import Validator


class CalculatorBackend:
    def __init__(self):
        self.validator = Validator()

    def calc(self, expression: str) -> int | float:
        is_valid_chars = self.validator.validate_chars(expression)

        if not is_valid_chars:
            raise InvalidCharsException(self.validator.get_invalid_chars())

        try:
            return eval(expression, {'__builtins__': None}, {})
        except Exception as e:
            raise InvalidExpression(expression) from e


if __name__ == '__main__':
    calc = CalculatorBackend()

    try:
        res = calc.calc('1/0')
    except InvalidCharsException as e:
        print(e)
    except InvalidExpression as e:
        print(e)
    # print(res)
