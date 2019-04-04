class Basic_arithmetic_calc:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def operations(self):
        print('Available operations:')
        print('1. Add')
        print('2. Sub')
        print('3. Mul')
        print('4. Div')

    def add_values(self, x, y):
        result = x + y
        print(f'{x} + {y} = {result}')
        # return result

    def sub_values(self, x, y):
        result = x - y
        print(f'{x} - {y} = {result}')
        # return result

    def mul_values(self, x, y):
        result = x * y
        print(f'{x} * {y} = {result}')
        # return result

    def div_values(self, x, y):
        result = x / y
        print(f'{x} / {y} = {result}')
        # return result