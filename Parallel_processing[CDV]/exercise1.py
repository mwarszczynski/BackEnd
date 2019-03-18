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

def read_value(x):
    y = str()
    for j in x:
        if(j.isdecimal()):
            y += dict_word[j] + ' '
    return y

x = input('Enter the number:\n')

print(read_value(x))


