class InvalidExpression(Exception):
    def __init__(self, expression):
        self.__expression = expression

    def __str__(self):
        return f'Invalid expression: "{self.__expression}". {self.__cause__}.'