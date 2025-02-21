from validator import Validator


class CalculatorBackend:
    def __init__(self):
        self.validator = Validator()

    def calc(self, expression: str) -> int | float:
        is_valid_chars = self.validator.validate_chars(expression)

        if not is_valid_chars:
            raise ValueError(f'Invalid characters in "{expression}": {self.validator.get_invalid_chars()}')

        try:
            return eval(expression, {'__builtins__': None}, {})
        except Exception as e:
            raise ValueError(f'Invalid expression "{expression}": {e}') from e


if __name__ == '__main__':
    calc = CalculatorBackend()
    res = calc.calc('1+2=')
    print(res)
