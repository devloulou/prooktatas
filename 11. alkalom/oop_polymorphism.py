
from os import *


lista = [1,2,3]

my_dict = {"kulcs": "érték"}

my_string = "ricsi"

print(len(lista))
print(len(my_dict))


class Animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("Run")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def run(self):
        print("Dog run fast")
    
animal = Animal("Emu")

animal.run()
floki = Dog("Floki")
floki.run()