import time


def timer(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(function.__name__ + ' execution time is ' + str((end-start) * 1000 + ' mil sec.'))
        return result

    return wrapper


@timer
def multiply(numbers):
    result = []
    for num in numbers:
        result.append(num * num * num)
    return result


@timer
def summary(numbers):
    result = []
    for num in numbers:
        result.append(num + num + num)
    return result


@timer
def div(numbers):
    result = []
    for num in numbers:
        result.append(num / num)
    return result


array = range(1, 10)
print('Equal of summary: ', summary(array))
print('Equal of multiply: ', multiply(array))
print('Equal of multiply: ', div(array))
