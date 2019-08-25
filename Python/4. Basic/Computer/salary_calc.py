class Salary_calc:

    def __init__(self):
        self.tax = 0.27

    def data(self):
        try:
            gross_amount = int(input('Enter Your gross amount: '))
        except ValueError:
            print('You have to enter correct value')

        result = (gross_amount * 27) / 100
        x = gross_amount - result
        print(x)

        # salary = lambda x: x - (x * self.tax)
        # print('Your net earnings: ', (gross_amount))