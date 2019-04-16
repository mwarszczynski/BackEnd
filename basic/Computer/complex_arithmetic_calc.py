import math

class Complex_arithmetic_calc:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    global modulo_values, root_values, power_values

    def operations(self):
        num1 = int(input('Enter number: '))
        num2 = int(input('Enter number: '))

        print('Available operations:')
        print('1. Modulo')
        print('2. Root')
        print('3. Power')

        detail_choice = int(input('Which operation?: '))
        if detail_choice == 1:
            modulo_values(num1, num2)
        elif detail_choice == 2:
            root_values(num1, num2)
        elif detail_choice == 3:
            power_values(num1, num2)
        else:
            print('Nothing has been selected')

    def modulo_values(x ,y):
        result = x % y
        print(f'{x} modulo {y} = {result}')

    def root_values(x ,y):
        result1 = math.sqrt(x)
        result2 = math.sqrt(y)
        print(f'Root of value {x} = {result1}')
        print(f'Root of value {y} = {result2}')

    def power_values(x ,y):
        result = x ** y
        print(f'{x} ** {y} = {result}')