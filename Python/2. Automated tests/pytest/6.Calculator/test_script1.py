import pytest
from script1 import Calculator, CalculatorError, MessageLongError


@pytest.fixture
def result():
    result = Calculator()
    return result

@pytest.mark.parametrize('num1, num2, expected', [
    (1, 1, 2),
    (3, 3, 6),
    (12.5, 12.5, 25),
])
def test_add_complex(result, num1, num2, expected):
    result.add(num1, num2)
    assert result

def test_div(result):
    with pytest.raises(Exception):
        result.div(2, 0)

@pytest.mark.skip
def test_tweet(result):
    with pytest.raises(Exception):
        result.tweet('Witamy')




















































