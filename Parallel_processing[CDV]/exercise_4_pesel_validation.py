# wagi potrzebne do obliczenia sumy kontrolnej nr Pesel
pesel_number_weight = ['1','3','7','9','1','3','7','9','1','3']
mul_result = []
# const - stała wartość pobrana ze wzoru do obliczania poprawności numeru Pesel
b = 10

def set_as_list(number):
    global pesel_number
    print(f'Numer pesel ktory podales: "{pesel_number}".')
    pesel_number = (list(str(pesel_number)))
    # return pesel_number

def calculate_scales(number):
    for x in range(len(pesel_number_weight)):
        result = int(pesel_number_weight[x]) * int(pesel_number[x])
        mul_result.append(result)

def add_multiplied_values(number):
    sum_result = sum(mul_result)
    print('Wynik zsumowania elementow listy: ',sum_result)
    modulo_result = sum_result % b
    print('Wynik dzielenia modulo: ',modulo_result)

    if(b - modulo_result) == int(pesel_number[10]):
        print('Numer Pesel poprawny!')
    else:
        print('Numer Pesel niepoprawny')

def show_basic_information(number):
    # print('Rok urodzenia',pesel_number[0],pesel_number[1])
    pesel_number[0:1] = [''.join(pesel_number[0:2])]
    # print(pesel_number[0:2])


pesel_number = input('Podaj Pesel: \n')

# Przerabiamy str(Pesel) do listy, zeby pozniej pomnozyc
set_as_list(pesel_number)
# wywolujemy funkcje, ktora pomnozy wagi * pesel i wstawi wyniki w tablice
calculate_scales(pesel_number_weight)
# Funkcja sumuje wartosci tablicy i wylicza modulo z otrzymanego wyniku, nastepnie sprawdza poprawnosc sumy kontrolnej.
add_multiplied_values(mul_result)
# Przedstawia dane na podstawie numeru Pesel
show_basic_information(pesel_number)

print('===',pesel_number)