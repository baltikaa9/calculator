import re


class Validator:
    __invalid_chars = None

    def get_invalid_chars(self) -> list | None:
        return self.__invalid_chars

    def validate_chars(self, expression: str) -> bool:
        match = re.findall(r'([^0-9+\-*/().% ]+)', expression, re.MULTILINE)
        if match:
            self.__invalid_chars = match
            return False
        return True


if __name__ == '__main__':
    validator = Validator()
    is_valid = validator.validate_chars('1+2=')

    if not is_valid:
        raise ValueError(f'Invalid characters in expression: {validator.get_invalid_chars()}')
