class Tax_Calc:

    def __init__(self):
        self.tax1 = 0.07
        self.tax2 = 0.23

    global smaller_tax, bigger_tax, operations

    def amount(self):
        try:
            self.amount = float(input('Enter the amount to be taxed: '))
            operations(self.amount)
        except ValueError:
            print('You have to enter correct number')

    def operations(self):
        print('1. Count tax 7%')
        print('2. Count tax 23%')

        detail_choice = int(input('Select one of the two: '))
        if detail_choice == 1:
            smaller_tax(self, self.amount)
        elif detail_choice == 2:
            bigger_tax(self, self.amount)
        else:
            print('Wrong')

    def smaller_tax(self, amount):
        after_tax1 = amount - (amount * self.tax1)
        print(f'Amount after taxed is {after_tax1}.')

    def bigger_tax(self, amount):
        after_tax2 = amount - (amount * self.tax2)
        print(f'Amount after taxed is {after_tax2}.')
