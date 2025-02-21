from exceptions.invalid_chars_exception import InvalidCharsException
from exceptions.invalid_expression import InvalidExpression
from exceptions.repeated_operators_exception import RepeatedOperatorsException
from exceptions.invalid_startwith_exception import InvalidStartwithException
from exceptions.invalid_endwith_exception import InvalidEndwithException
from validator import Validator


class CalculatorBackend:
    def __init__(self, validator: Validator = None):
        self.__validator = validator

    def calc(self, expression: str) -> int | float:
        if self.__validator:
            if not self.__validator.validate_chars(expression):
                raise InvalidCharsException(self.__validator.invalid_chars)

            if not self.__validator.validate_repeated_operators(expression):
                raise RepeatedOperatorsException(self.__validator.repeated_operators)

            if not self.__validator.validate_startwith(expression):
                raise InvalidStartwithException(self.__validator.invalid_startwith)

            if not self.__validator.validate_endwith(expression):
                raise InvalidEndwithException(self.__validator.invalid_endwith)

        try:
            return eval(expression, {'__builtins__': None}, {})
        except Exception as e:
            raise InvalidExpression(expression) from e


if __name__ == '__main__':
    calc = CalculatorBackend(Validator())

    try:
        res = calc.calc('*1')
    except InvalidCharsException as e:
        print(e)
    except InvalidExpression as e:
        print(e)
    # print(res)
