list1 = []
list2 = []
list3=list1

# print(id(list1))
# print(id(list2))
# print(id(list3))
# exit()
 
if (list1 == list2):
    print("True")
else:
    print("False")
 
if (list1 is list2):
    print("True")
else:
    print("False")
 
if (list1 is list3):
    print("True")
else:   
    print("False")
 
list3 = list3 + [2]

list3.append(1)

print(f"list1: {list1}")
print(f"list1: {list3}")
 
if (list1 is list3):
    print("True")
else:   
    print("False")

# #and or not
a = 0
b = 0



if (a > 1) or (b > 1) or (b == 3) or (1 == 0):
    print(a+b)
else:
    print("else ág")

if (a > 1) and (b > 1) and (b == 3) and (1 == 1):
    print(a+b)
else:
    print("else ág")

print(1==0)

if (a == 0) and (b == 0) and (b == a) and (1 == 1):
    print(a == 0)
    print(b == 0)
    print(a+b)
else:
    print("else ág")

if ((a == 0) and (b == 0)) or ((b == a) and (1 == 1)):
    print(a == 0)
    print(b == 0)
    print(a+b)
else:
    print("else ág")


a = False

 
# And igazságtába        OR                         Not
# True True   - True    True True - True            True - False
# True False  - False   True False - True           False - True
# False True  - False   False True - True
# False False - False   False False - False

a = 2

a = [1]
a = [] # 0

a = (None) # false
a = () # false
a = [0] # true
a = (0) #false

a = {0} # true

a = (0,1) # true

if a:
    print(True)
else:
    print(False)

####################################################

c = True if a else False

print(c)

szam1= 5
szam2= 4
osszeg = 10

osszeg = szam1 + szam2 if szam2 > szam1 else osszeg

#ha(a>b;"igaz ág";"hamis ág")
print()

if szam2 > szam1:
    osszeg = szam1 + szam2
else:
    osszeg = szam1 - szam2
#ternary operator

#inline if else

if szam2 > szam1: osszeg = szam1 + szam2
else: osszeg = szam1 - szam2

print(osszeg)


x = 5
result = 'High' if x > 10 else 'Low'

print(result)

###########
#ciklusok
#comprehension műveletek (# generátor függvények)
#python sturktúra kialakítás: névterek és a hozzá szükséges struktúra
#függvények denifinálása
#packing és unpacking
#generátor függvények