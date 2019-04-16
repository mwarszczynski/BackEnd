#
# def cars_count(dictionary):
#     belts = list(dictionary.values())
#     for belt in belts:
#         num = belts.count(belt)
#         print(f'The are {num} {belt} belts')
#
# def cars_into(dictionary):
#     for key,val in dictionary.items():
#         print(f'It is {key} and {val}.')
#
# cars = {}
#
# while True:
#     cars_name = input('Enter cars name')
#     cars_model = input('Enter cars model')
#     print(f'You write {cars_name} and {cars_model}')
#     cars[cars_name] = cars_model
#
#     ask = input('Want to add another one? (y/n)')
#     if ask == 'y':
#         continue
#     else:
#         break
#
# # cars_into(cars)
# cars_count(cars)


# prizes = [5,10,50,100,1000]
# dbl_prizes = []
# for prize in prizes:
#     dbl_prizes.append(prize*2)
#
# print(dbl_prizes)
#
#
# dbl_prizes = [ prize*2 for prize in prizes ]
# print(dbl_prizes)
#
#
#
#
# nums = [1,2,3,4,5,6,7,8,9,10]
# squared_even_nums = []
#
# for num in nums:
#     if (num**2) % 2 == 0:
#         squared_even_nums.append(num**2)
#
# print(squared_even_nums)
#
#
# squared_even_nums = [num ** 2 for num in nums if(num**2) % 2 == 0]
# print(squared_even_nums)

# from random import shuffle
#
# def jumble(word):
#     anagram = list(word)
#     shuffle(anagram)
#     return ''.join(anagram)
#
# words = ['beetroot','carrots','potatoes']
# anagrams = []
#
#
# print(list(map(jumble, words)))

# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)

# jumble(words)

# def kwadrat(x):
#     return x**2
#
# kwadraty = map(kwadrat, range(10))
# list(kwadraty)


# income = [10, 30, 75]
#
# def double_money(dollars):
#     return dollars * 2
#
# new_income = list(map(double_money, income))
# print(new_income)
#
#
# for item in income:
#     return income * 2

# grades = ['A','B','F','C','F','A']
#
# def remove_fails(grade):
#     return grade != 'F'
#
# # print(list(filter(remove_fails, grades)))
#
# filtered_grades = []
# for grade in grades:
#     if grade != 'F':
#         filtered_grades.append(grade)
#
# print(filtered_grades)


# nums = [1,2,3,4,5,6]

# def square(n):
#     return n * n

# print(list(map(square, nums)))

# Lambda
# print(lambda x: nums * nums)

# print(list(map(lambda n: n * n, nums)))


# def inna_funkcja():
#     print("inna funkcja")
#
# def dekorator(obj):
#     return inna_funkcja
#
# @dekorator
# def funkcja():
#     print("hello")
#
# funkcja()



# def dekorator(obj):
#     def inna_funkcja():
#         obj()
#         print("world")
#     return inna_funkcja
#
# @dekorator
# def funkcja():
#     print("hello")
#
# funkcja()



class WebMock():
    def get(self, url):
        return url + " always works!"

def cache(wrapped_function):
    def wrapper(web, url):
        if url in "https://chyla.org/":
            return "It work's!"
        else:
            return wrapped_function(web, url)
    return wrapper

@cache
def get_web_page(web, url):
    return web.get(url)


web = WebMock()

page = get_web_page(web, "chyla.org")
print("chyla.org content: " + page)

page = get_web_page(web, "google.com")
print("google.com content: " + page)






















