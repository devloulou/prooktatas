# Python program to demonstrate
# use of class method and static method.
from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	# a class method to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)
	
	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print (person1.age)
print (person2.age)

# print the result
print (Person.isAdult(22))


class Test:
    def __init__(self, age):
        self.__age=age

test = Test(10)
print(test._Test__age)


1

class B:
    def __init__(self):
        self.__private = 0 
    def __private_method(self):
        '''A private method via inheritance'''
        return ('{!r}'.format(self))
    def internal_method(self):
        return ('{!s}'.format(self))

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1
    def __private_method(self):
        return 'Am from class C'

c = C()
print(c.__dict__)
b = B()
print(b.__dict__)
print(b._B__private)
print(c._C__private_method())