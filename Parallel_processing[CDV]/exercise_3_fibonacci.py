values = [1,1]

def fibonacci_string(y):
    for x in range(1, y):
        values.append(values[-1] + values[-2])
    print(', '.join(str(j) for j in values))

def check_value_from_input():
    try_count = 0

    while True:
        try:
            final_range = int(input('Enter the final range of loop:\n'))
            fibonacci_string(final_range)
            break
        except(TypeError, ValueError):
            print('You have to enter the correct value - which is integer')
            try_count += 1
        if try_count > 3:
            print('You typed an incorrect password three times in a row. Good Bye!')
            break

check_value_from_input()
