from basic_arithmetic_calc import Basic_arithmetic_calc
from complex_arithmetic_calc import Complex_arithmetic_calc
from tax_calc import Tax_Calc
from salary_calc import Salary_calc

def show_options():
    print('1. Basic operations (Add, Sub, Mul, Div)')
    print('2. Complex operations (Modulo, root, power)')
    print('3. Tax calculator')
    print('4. Salary calculator')
    print('5. Fuel combustion calculator')
    print('6. Random Dice throw')

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

show_options()
choice = int(input('Choose operation: '))

if choice == 1:
    option1 = Basic_arithmetic_calc()
    option1.operations()

    detail_choice = int(input('Which operation?: '))
    if detail_choice == 1:
        option1.add_values(num1, num2)
    elif detail_choice == 2:
        option1.sub_values(num1, num2)
    elif detail_choice == 3:
        option1.mul_values(num1, num2)
    elif detail_choice == 4:
        option1.div_values(num1, num2)
    else:
        print('Nothing has been selected')

if choice == 2:
    option2 = Complex_arithmetic_calc()
    option2.operations()

    detail_choice = int(input('Which operation?: '))
    if detail_choice == 1:
        option2.modulo_values(num1, num2)
    elif detail_choice == 2:
        option2.root_values(num1, num2)
    elif detail_choice == 3:
        option2.power_values(num1, num2)
    else:
        print('Nothing has been selected')

if choice == 3:
    option3 = Tax_Calc()
    option3.amount()
    option3.operations()

if choice == 4:
    option4 = Salary_calc()
    option4.data()

# Kalkulator wynagrodzenia
# - salary_calc


# Kalkulator spalania paliwa
# - fuel_combustion_calc


# Rzuć kostką
# - dice_throw