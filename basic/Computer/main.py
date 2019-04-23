import os
import pathlib

import shutil

from basic_arithmetic_calc import Basic_arithmetic_calc
from complex_arithmetic_calc import Complex_arithmetic_calc
from tax_calc import Tax_Calc
from salary_calc import Salary_calc
from fuel_combustion_calc import Fuel_Combustion
# from dice_throw import Dice_Throw

logs_temporary = 'logsDir'

def create_logs_folder():
    global current_dir
    current_dir = os.getcwd()
    print('You are running script in', current_dir)

    try:
        # Creating target directory
        os.mkdir(logs_temporary)
        print('Directory "', logs_temporary, '" created.')
    except FileExistsError:
        print('Directory "', logs_temporary, '" already exists!')

def show_options():
    print('\n1. Basic operations (Add, Sub, Mul, Div)')
    print('2. Complex operations (Modulo, root, power)')
    print('3. Tax calculator')
    print('4. Salary calculator')
    print('5. Fuel combustion calculator')
    print('6. Random Dice throw\n')

def copy_logs_to_dir():
    shutil.copy2('./logs.log', logs_temporary)

create_logs_folder()
show_options()
# copy_logs_to_dir()

choice = int(input('Choose operation: '))

if choice == 1:
    option1 = Basic_arithmetic_calc()
    option1.operations()

elif choice == 2:
    option2 = Complex_arithmetic_calc()
    option2.operations()

elif choice == 3:
    option3 = Tax_Calc()
    option3.amount()

elif choice == 4:
    option4 = Salary_calc()
    option4.data()

elif choice == 5:
    option5 = Fuel_Combustion()
    km_quantity = int(input('How many kilometers: '))
    oil_type = input('Enter type: (petrol/diesel/oil)')
    combust = int(input('Enter combust: '))

    option5.cost(km_quantity, oil_type, combust)

# elif choice == 6:
#     option6 = Dice_Throw()

else:
    print('Wrong')

copy_logs_to_dir()
# Kalkulator spalania paliwa
# - fuel_combustion_calc


# Rzuć kostką
# - dice_throw