#decorator fogalma:
# Egy függvény, amely tulajdonságokkal ruház fel egy másik függvényt,
# "viselkedést" ad neki, anélkül, hogy az eredeti függvényt megváltoztatnánk

# szintatkitkája

# @my_decorator
# def my_func(param1):
#     return 2*2
#############################################

def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')

    return wrapper

def kiir():
    name = "Ricsi"
    print(f"My name is {name}")

#kiir = start_end_decorator(kiir)

#############################################

import timeit

def start_end_decorator(func):
    def wrapper():
        start = timeit.timeit()
        func()
        end = timeit.timeit()
        print(end - start)

    return wrapper

@start_end_decorator
def kiir():
    name = "Ricsi"
    print(f"My name is {name}")

# kiir()
# print()

#kiir()

import functools

def start_end_decorator_2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print(result)
        print('End')
        return result
    return wrapper


@start_end_decorator_2
@start_end_decorator_2
@start_end_decorator_2
def add_number(x):
    return x + 10

# temp = start_end_decorator_2(add_number)
# print(temp)

# print(temp(5))

result = add_number(5)

#print(result)

print(add_number.__name__)


def repeater(num):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeater(5)
def greetings(name):
    print(f"Hello {name}")


#greetings("Ricsi")

