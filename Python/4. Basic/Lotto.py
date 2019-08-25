import random, os

def randFunc():
    x = 0
    numbers = set()
    numbersList = []

    try:
        numbersCount = int(input('Podaj ilosc typowanych liczb: '))
        maksLiczba = int(input('Podaj maksymalna losowana wartosc: '))
        if numbersCount > maksLiczba:
            print('You cannot set "ileLiczb" higher than "maksLiczba".')
    except ValueError as e:
        print(e)
        exit()

    while x < numbersCount:
        x = x + 1
        randomedNumber = random.randint(1 , maksLiczba)
        numbers.add(randomedNumber)
        print('Index number', x,':',randomedNumber)

    saveToFile(str(numbers))

# Function save data in file.
def saveToFile(data):
    try:
        with open('Results.txt', 'w+') as file:
            file.write(data)

    except FileExistsError as e:
        print(e)

    except OSError as e:
        print(e)
        pass


print(randFunc())

