class CalculatorError(Exception):
    '''An Exception Class for Calculator'''


class MessageLongError(Exception):
    '''An Exception Class for To Long Message'''


class Calculator(object):
    '''A calculator'''

    def add(self,a ,b):
        '''Adding two values'''
        return a + b

    def subtrack(self, a , b):
        '''Sub two values'''
        return a - b

    def multiply(self, a, b):
        '''Mul two values'''
        return a * b

    def div(self, a, b):
        '''Div two values'''
        if b == 0:
            raise ZeroDivisionError('You are trying do div over 0!')
        return a / b

    def modulo(self, a, b):
        '''Modulo'''

    def tweet(self, msg):
        '''Push tweet on tweeter'''
        if len(msg) > 5:
            raise MessageLongError()
        return msg

    def print_smth(self):
        print('Its some kind of message!')





































