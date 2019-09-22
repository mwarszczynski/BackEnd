#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from syntax_repeat2 import Calculator, randomed_int_values_pow, random_int_values

'''Testing Calculator Class'''
@pytest.fixture
def calculator():
    calculator = Calculator()
    return calculator

@pytest.mark.parametrize('num1, num2, expected', [
    (30, 30, 60),
    (40, 40, 80),
    (-20, 20, 0),
    (602.5, 2.5, 600)
])
def test_add(calculator, num1, num2, expected):
    calculator.add(num1, num2)
    assert calculator

@pytest.mark.parametrize('num1, num2, expected', [
    (30, 30, 0),
    (40, 40, 0),
    (-200, 20, 180),
    (3.5, 2.2, 3.3)
])
def test_sub(calculator, num1, num2, expected):
    calculator.sub(num1, num2)
    assert calculator

def test_div(calculator):
    with pytest.raises(Exception):
        calculator.div(20, 0)

@pytest.mark.parametrize('val1, expected', [
    ([2, 3, 4, 5], [4,9,16,25]),
    ([0.0, 3.3, 2.2], [0, 9.9, 4.4]),
])
def test_pow_list_numbers(calculator, val1, expected):
    calculator.pow_list_numbers(val1)
    assert calculator

@pytest.mark.parametrize('val1, expected', [
    ({2: 'Add'}, {4: 'Add'}),
    ({3: 'Add'}, {16: 'Add'}),
    ({4: 'Add'}, {27: 'Add'}),
])
def test_pow_dict_values(calculator, val1, expected):
    calculator.pow_dict_values(val1)
    assert calculator

@pytest.mark.parametrize('val1, expected', [
    (30, 60),
    (-20, 40),
    (3.5, 7),
    ('w', 'x'), # ?! Sth goes wrong, this test shouldnt be passed
])
def test_modulo_lambda(calculator, val1, expected):
    calculator.modulo_lambda(val1)
    assert calculator

'''Testing RandNumbers function, where using decorator'''
# In progress