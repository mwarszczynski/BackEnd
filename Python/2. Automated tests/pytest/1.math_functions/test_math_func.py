import math_func
import pytest


@pytest.mark.parametrize('num1, num2, expected',
                         [
                             (8, 2, 10),
                             ('Hello', ' World', 'Hello World'),
                             (10.5, 25.5, 36)
                         ])
def test_add(num1, num2, expected):
    assert math_func.add(num1, num2) == expected


@pytest.mark.parametrize('num1, num2, expected',
                         [
                             (30, 30, 0),
                             (212, 213, -1),
                             (-1, -1, 0)
                         ])
def test_sub(num1, num2, expected):
    assert math_func.sub(num1, num2) == expected


@pytest.mark.parametrize('num1, num2, expected',
                         [
                             (-2, 4, -8),
                             (0, 0, 0),
                             (-3, -3, 9)
                         ])
def test_mul(num1, num2, expected):
    assert math_func.mul(num1, num2) == expected


@pytest.mark.parametrize('num1, num2, expected',
                         [
                             (2, 4, 0.5),
                             (20, 40, 0.5),
                             (1, 1, 1)
                         ])
def test_div(num1, num2, expected):
    assert math_func.div(num1, num2) == expected


@pytest.mark.parametrize('num1, expected',
                         [
                             (3, 9),
                             (-4, 16)
                         ])
def test_pow(num1, expected):
    assert math_func.pow(num1) == expected



def test_add_string():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    assert 'Hello' in result
    assert type(result) is str
