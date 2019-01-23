# 1. First player invents word, and write - how many char are contained
# 2. If second player will guess the letter, first player appends this char to 'guessed'
# 3. If quantity of guesses is equal to the number of words given to the player - break ('hangman done')
import time

password = ''           # password to guess
toGuess = ''            # Defining the secret word
hitCounter = 10         # variable that counts how many attempts have occured
badGuess = 0
i = 0                   # while loop counter

time.sleep(1)
print('Hello, lets play Hangman!\nYou have got', hitCounter, 'guess.\n')
time.sleep(1)

# In first step we have to check that 'secred word' is not int
while True:
    toGuess = input('Type the password: ')
    if toGuess.isdigit():
        print('You have to type string')
    else:
        print('Good')
        password = toGuess
        break

# Then, user try go guess one letter of the word
while i < hitCounter:
    i = i + 1
    x = input('Guess one word: ')
    if x in password:
        print('Good, mentioned letter "%s" is there!' % x)
        # goodGues = goodGues + 1   # -------------------------> next commit, lets start from here <--------------------------
    else:
        badGuess = badGuess + 1
        print('Unfortunately, secret word does not containt "%s". Number of errors = %s.' % (x,badGuess))









