import random

class Dice_Throw:


    # count_quantity = int(input('How many times do You want do throw?' ))

    random_results = []
    count = 0

    while count < count_quantity:
        random_results.append(random.randint(1,6))
        count += 1

    print(random_results)
