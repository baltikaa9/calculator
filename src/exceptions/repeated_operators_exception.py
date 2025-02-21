class RepeatedOperatorsException(Exception):
    def __init__(self, chars: list[str]):
        self.__chars = chars

    def __str__(self):
        return f'Неверные операторы: ({', '.join(self.chars)})'

    @property
    def chars(self) -> list[str]:
        return self.__chars
