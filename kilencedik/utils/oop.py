# OOP principles
# absztakció: 
class Dog:

    def __init__(self, name):
        self.name = name 
        print(self.name + " was adopted.")

    def bark(self):
        print("woof!")


# we don't care how it works just bark
spot = Dog("spot") #=> spot was adopted. 
spot.bark() #=> woof! 

#################
# inheritencia:
class Animal:

    def __init__(self, name):
        self.name = name 
        print(self.name + " was adopted.")

    def run(self):
        print("running!")


class Dog(Animal):

    def __init__(self):
        super().init 

    def bark(self):
        print("woof!")


# new dog behavior inherited from Animal parent class 
spot = Dog("spot") #=> spot was adopted. 
spot.run() #=> running! 

#########################
# encapsulation
# keeping all the state, variables,
# and methods private unless declared to be public.

class Fish:

    def __init__(self):
        self.__size = "big"

    def get_size(self):
        print("I'm a " + self.__size + " fish")

    def set_size(self, new_size):
        self.__size = new_size 

# using the getter method
oscar = Fish()
oscar.get_size()  #=> I'm a big fish

# change the size 
bert = Fish()
bert.__size = "small" 
bert.get_size() #=> I'm a big fish

# using setter method
fin = Fish()
fin.set_size("tiny")
fin.get_size() #=> I'm a tiny fish


######################################
#Polymorphism
class Animal:

    def __init__(self, name):
        self.name = name 
        print(self.name + " was adopted.")

    def run(self):
        print("running!")


class Turtle(Animal):

    def __init__(self):
        super().init 

    def run(self):
        print("running slowly!")


# we get back an interesting response 
tim = Turtle("tim") #=> tim was adopted. 
tim.run() #=> running slowly!