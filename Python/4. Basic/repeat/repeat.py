import random


class OpenFile(object):

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


class Calculator(object):
    '''Calculator'''

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError('Not div over "0".')
        return a / b

    def pow_list_numbers(self, numbers_list):
        result = [list_numbers_doubled.append(number) for number in numbers_list]

    def pow_dict_values(self, values_dict):
        for k, v in values_dict.items():
            print(k**k)

    def modulo_lambda(self, arg1):
        double = lambda arg1: arg1 * 2
        print(double(arg1))


def randomed_int_values_pow(f):
    def inner(f):
        return f() ** 2
    return inner

@randomed_int_values_pow(2)
def random_int_values():
    rand_values = random.choice([1, 2, 3])
    # with OpenFile('logs.txt', 'w') as file_open:
    #     file_open.write(f'Wylosowana liczba to: {rand_values}.')
    return rand_values


list_numbers_doubled = []
dict_values = {
    1: 'Add',
    2: 'Sub',
    3: 'Mul',
    4: 'Div'
}
rand_numbers_list = []

calculator = Calculator()
calculator.pow_list_numbers([1,2,3,4,5])
calculator.pow_dict_values(dict_values)
calculator.modulo_lambda(2)

print(list_numbers_doubled)
print(random_int_values)











