import math

class Complex_arithmetic_calc:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def operations(self):
        print('Available operations:')
        print('1. Modulo')
        print('2. Root')
        print('3. Power')

    def modulo_values(self,x ,y):
        result = x % y
        print(f'{x} modulo {y} = {result}')

    def root_values(self,x ,y):
        result1 = math.sqrt(x)
        result2 = math.sqrt(y)
        print(f'Root of value {x} = {result1}')
        print(f'Root of value {y} = {result2}')

    def power_values(self,x ,y):
        result = x ** y
        print(f'{x} ** {y} = {result}')