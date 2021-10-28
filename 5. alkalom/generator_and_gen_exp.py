import sys

lista = []

for item in range(1, 10):
    lista.append(item)

my_list = [item for item in range(1, 3)]

# lazy evaluation
my_generator_expression = (item for item in range(1, 3))


# for item in my_generator_expression:
#     print(item)

# print(next(my_generator_expression))
# print(next(my_generator_expression))
# print(next(my_generator_expression))


# custom generator function

def kiir():
    print("ricsi")
    return '1'

def my_generator():
    yield '2'

# print(type(kiir))
# print(type(my_generator))

# a = kiir()

# print(a)

b = my_generator()
# print(b)

#print(next(b))
#print(next(b))
def vissza_szamol(szam):
    print("Kezdes")
    return None

def vissza_szamol(szam):
    print("Kezdes")
    while True:
        yield szam
        szam -= 1

count = vissza_szamol(5)

print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))


print(type(my_list))
print(type(my_generator_expression))

# print(my_list)
# print(my_generator_expression)

print(sys.getsizeof(my_list))
print(sys.getsizeof(my_generator_expression))

