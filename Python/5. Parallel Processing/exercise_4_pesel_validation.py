# wagi potrzebne do obliczenia sumy kontrolnej nr Pesel
pesel_number_weight = ['1','3','7','9','1','3','7','9','1','3']
mul_result = []
# const - stała wartość pobrana ze wzoru do obliczania poprawności numeru Pesel
b = 10

def set_as_list(number):
    global pesel_number
    print(f'Numer pesel ktory podales: "{pesel_number}".')
    pesel_number = (list(str(pesel_number)))

def calculate_scales(number):
    for x in range(len(pesel_number_weight)):
        result = int(pesel_number_weight[x]) * int(pesel_number[x])
        mul_result.append(result)

def add_multiplied_values(number):
    sum_result = sum(mul_result)
    print(f'Wynik zsumowania elementow listy {sum_result}.')
    modulo_result = sum_result % b
    print(f'Wynik zsumowania elementow listy {modulo_result}.')

    if(b - modulo_result) == int(pesel_number[10]):
        print('Numer Pesel poprawny!')
    else:
        print('Numer Pesel niepoprawny')

def show_basic_information(number):
    year_birth_date = ''.join(pesel_number[0:2])
    month_birth_date = ''.join(pesel_number[2:4])
    day_birth_date = ''.join(pesel_number[4:6])
    what_sex_sum = int(pesel_number[6]) + int(pesel_number[7]) + int(pesel_number[8]) + int(pesel_number[9])

    if what_sex_sum % 2 == 1:
        what_sex = 'Male sex'
    else:
        what_sex = 'Female sex'

    print(f'Your born date is {day_birth_date}.{month_birth_date}.{year_birth_date} and You are {what_sex}.')


pesel_number = input('Podaj Pesel: \n')

# Przerabiamy str(Pesel) do listy, zeby pozniej pomnozyc
set_as_list(pesel_number)
# wywolujemy funkcje, ktora pomnozy wagi * pesel i wstawi wyniki w tablice
calculate_scales(pesel_number_weight)
# Funkcja sumuje wartosci tablicy i wylicza modulo z otrzymanego wyniku, nastepnie sprawdza poprawnosc sumy kontrolnej.
add_multiplied_values(mul_result)
# Przedstawia dane na podstawie numeru Pesel
show_basic_information(pesel_number)
