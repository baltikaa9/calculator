import re


class Validator:
    __current_invalid_chars: list[str] = None
    __current_repeated_operators: list[str] = None
    __current_invalid_startwith: list[str] = None
    __current_invalid_endwith: list[str] = None

    @property
    def invalid_chars(self) -> list[str] | None:
        return self.__current_invalid_chars

    @property
    def repeated_operators(self) -> list[str] | None:
        return self.__current_repeated_operators

    @property
    def invalid_startwith(self) -> list[str] | None:
        return self.__current_invalid_startwith

    @property
    def invalid_endwith(self) -> list[str] | None:
        return self.__current_invalid_endwith

    def __validate(self, expression: str, regex: str, error_attr: str) -> bool:
        match = re.findall(regex, expression, re.MULTILINE)
        if match:
            setattr(self, error_attr, match)
            return False
        return True

    def validate_chars(self, expression: str) -> bool:
        return self.__validate(''.join(set(expression)), r'([^0-9+\-*/(). ]+)', '_Validator__current_invalid_chars')

    def validate_repeated_operators(self, expression: str) -> bool:
        return self.__validate(expression, r'(\+{2,}|\-{2,}|\*{3,}|/{3,})', '_Validator__current_repeated_operators')

    def validate_startwith(self, expression: str) -> bool:
        return self.__validate(expression, r'^[*/]', '_Validator__current_invalid_startwith')

    def validate_endwith(self, expression: str) -> bool:
        return self.__validate(expression, r'[+\-*/]$', '_Validator__current_invalid_endwith')


if __name__ == '__main__':
    validator = Validator()
    is_valid = validator.validate_startwith('*1')

    print(is_valid)

    print(validator.invalid_startwith)

    # if not is_valid:
    #     raise ValueError(f'Invalid characters in expression: {validator.invalid_chars}')
