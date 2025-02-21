import pytest

from validator import Validator


class TestValidator:
    @pytest.fixture
    def validator(self) -> Validator:
        return Validator()

    @pytest.mark.parametrize(
        'expression, is_valid, invalid_chars',
        [
            ('1+2', True, None),
            ('10-5*2', True, None),
            ('(3+5)/2', True, None),
            ('-42+18', True, None),
            ('2**2', True, None),
            ('2***2', True, None),
            ('2^2', False, ['^']),
            ('1+2=', False, ['=']),
            ('a+1', False, ['a']),
            ('1,2', False, [',']),
            ('1.2', True, None),
            ('10%', False, ['%']),
            ('===', False, ['='])
        ]
    )
    def test_validate_expression(
            self,
            validator: Validator,
            expression: str,
            is_valid: bool,
            invalid_chars: list | None
    ) -> None:
        assert validator.validate_chars(expression) == is_valid
        assert validator.invalid_chars == invalid_chars

    @pytest.mark.parametrize(
        'expression, is_valid, repeated_operators',
        [
            ('1**2', True, None),
            ('1***2', False, ['***']),
            ('1//2', True, None),
            ('1///2', False, ['///']),
            ('1++2', False, ['++']),
            ('1+++2', False, ['+++']),
            ('1--2', False, ['--']),
            ('1---2', False, ['---']),
        ]
    )
    def test_validate_operators(
            self,
            validator: Validator,
            expression: str,
            is_valid: bool,
            repeated_operators: list | None
    ) -> None:
        assert validator.validate_repeated_operators(expression) == is_valid
        assert validator.repeated_operators == repeated_operators

    @pytest.mark.parametrize(
        'expression, is_valid, startwith',
        [
            ('+1', True, None),
            ('-1', True, None),
            ('*1', False, ['*']),
            ('/1', False, ['/']),
            ('1+', True, None),
        ]
    )
    def test_validate_startwith(
            self,
            validator: Validator,
            expression: str,
            is_valid: bool,
            startwith: list | None
    ) -> None:
        assert validator.validate_startwith(expression) == is_valid
        assert validator.invalid_startwith == startwith

    @pytest.mark.parametrize(
        'expression, is_valid, endwith',
        [
            ('*1', True, None),
            ('1+', False, ['+']),
            ('1-', False, ['-']),
            ('1*', False, ['*']),
            ('1/', False, ['/']),
        ]
    )
    def test_validate_endwith(
            self,
            validator: Validator,
            expression: str,
            is_valid: bool,
            endwith: list | None
    ) -> None:
        assert validator.validate_endwith(expression) == is_valid
        assert validator.invalid_endwith == endwith
