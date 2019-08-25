dict_word = {
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine'
}

def recieve_value(x):
    temp = str()
    for i in x:
        if(i.isdecimal()):
            temp += dict_word[i] + ' \n'
    return temp

x = input('Enter the number:\n')

print(recieve_value(x))


