class InvalidEndwithException(Exception):
    def __init__(self, chars: list[str]):
        self.__chars = chars

    def __str__(self):
        return f'Выражение не должно заканчиваться на {', '.join(self.chars)}'

    @property
    def chars(self) -> list[str]:
        return self.__chars
