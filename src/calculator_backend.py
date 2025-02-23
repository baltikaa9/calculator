from src.exceptions.invalid_chars_exception import InvalidCharsException
from src.exceptions.invalid_expression import InvalidExpression


class CalculatorBackend:
    @staticmethod
    def calc(expression: str) -> int | float:
        try:
            return eval(expression, {'__builtins__': None}, {})
        except Exception as e:
            raise InvalidExpression(expression) from e


if __name__ == '__main__':
    calc = CalculatorBackend()

    try:
        res = calc.calc('*1')
    except InvalidCharsException as e:
        print(e)
    except InvalidExpression as e:
        print(e)
    # print(res)
