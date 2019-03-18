min_range = -20
max_range = 40

for i in range(min_range, max_range + 1, 5):
    fahrenheit = i * 1.8 + 32
    print('%s°C = %s°F' % (i, fahrenheit))
