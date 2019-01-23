# 1. First player invents word, and write - how many char are contained
# 2. If second player will guess the letter, first player appends this char to 'guessed'
# 3. If quantity of guesses is equal to the number of words given to the player - break ('hangman done')

# User have to enter the word, not int
while True:
    password = input('Type the password: ')
    if password.isdigit():
        print('You have to type string')
    else:
        print('Good')
        break


