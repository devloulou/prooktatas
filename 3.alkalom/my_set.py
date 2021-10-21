my_set = {}
#print(type(my_set))

my_set = set([1,2,3,4,5])

# a set: A set is a collection which is unordered, unchangeable, and unindexed. - Nem rendezett - nem őrzi meg a sorrendet; 
# nem változtathatóak az elemei 
# nincs indexálva
my_set.pop()
my_set.pop()
my_set.pop()

my_set.add(2)
my_set.add(7)
my_set.add(7)
my_set.pop()

print(my_set)

###############################################
# boolean

x = True
y = False
x = 10


x = 6

# if x > 5:
#     print("nagyobb")
#     if x == 6:
#         print("igen, 6")
#     else:
#         print("nem")
# else:
#     print("Nem nagyobb")
#     print()
    

# if x > 5:
#     print("nagyobb")
#     print("lefutott")

# if x == 6:
#     print("igen, 6")
#     print("lefutott")

# print("###########")

# if x > 5:
#     print("nagyobb")
# elif x == 6:
#     print("igen, 6")



# if x > 5:
#     print("nagyobb")
# else:
#     if x == 6:
#         print("igen, 6")
    

#is and or 

a = 4
b = 4




#nem python: > < != = <= >= 
#python: > < != == <= >=

print(id(a))
print(id(b))

a = 6

print(id(a))
print(id(b))

if b > a:
    print("nagyobb")

if a != b:
    print("nem egyenlő")

if a == b:
    print("egyenlő")

if a is b:
    print(a is b)
else:
    print("nem a is b")

if a > 2 or b <= 4:
    print(a+b)

#### is egyelő ==




#########################################################
