from abc import abstractmethod
import abc
import os
import sys

a = 10

class TestClass:

    b = 5

    def kiir(self):
        print(a)


my_class = TestClass()
#my_class.kiir()

#print(my_class.b)

def kiir():
    c = 20
    print(a)
    print(c)

##kiir()

# global
a = 10
x = 10
def kulso_fuggveny():
    valtozo = 1
    a = 12
    # local
    def belso_fuggveny():
        # enclosing scope        
        global a
        print(a)
        global x
        
        x -= 1
        print(x)
        if x > 10:
            kulso_fuggveny()
    
    belso_fuggveny()
    print(valtozo)
    print(x)


kulso_fuggveny()

def func():
    # local scope
    alma = "fa"
    print(alma)

    for item in range(0,0):
        dinnye = "föld"

    if 1 == 1:
        korte = "bokor"


    print(korte)
    print(dinnye)


func()