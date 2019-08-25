class calculate_tax():

    def __init__(self):
        self.tax1 = 0.07
        self.tax2 = 0.23

    def calculate_tax1(self, amount):
        part_of_result = self.tax1 * amount
        final_result = amount - part_of_result

        print('Amount before tax is equal {}.'.format(amount))
        print('Tax amount is equal to {}.'.format(round(part_of_result, 2)))
        print('Amount after tax is equal to {}'.format(round(final_result, 2)))

    def calculate_tax2(self, amount):
        part_of_result = self.tax2 * amount
        final_result = amount - part_of_result

        print('Amount before tax is equal {}.'.format(amount))
        print('Tax amount is equal to {}.'.format(round(part_of_result, 2)))
        print('Amount after tax is equal to {}'.format(round(final_result, 2)))

class calculate_day_salary():

    def __init__(self):
        self.work_days = 22         # Assumption that we are always working 22 days in month (it's sth like CONST)

    def calculate_salary1(self, cash_per_hour_gross, hours_quantity):
        # salary per day
        daily_salary = cash_per_hour_gross * hours_quantity
        # salary per week
        weekly_salary = daily_salary * work_days_per_week
        # salary per month
        monthly_salary = weekly_salary * work_weeks

        print('Your average daily salary is equal to {} gross.'.format(daily_salary))
        print('Your average weekly salary is equal to {} gross.'.format(weekly_salary))
        print('Your average monthly salary is equal to {} gross.'.format(monthly_salary))


work_days_per_week = 5
work_weeks = 4

# Creating new instance
wylicz = calculate_tax()
# 7% tax calculation
wylicz.calculate_tax1(100)
print('______________________')
# 23% tax calculation
wylicz.calculate_tax2(100)

print('______________________')
# Creating new instance
salary = calculate_day_salary()
# Check mothly salary
x = int(input('Pass your hourly salary: '))
y = int(input('Enter a daily number of hours: '))
# Calling the function that calculate user requirements
salary.calculate_salary1(x, y)












