#hasonlóan a C++-beli namespace-ekhez, a különböző nyelvi elemeknek 
# Pythonban is létezik struktúrája. A struktúra különböző szintjeit `.'-tal 
# választjuk el egymástól. A névterek általában láthatósági tartományokat is jelölnek.
#  névtér tulajdonképpen név -> objektum leképezések halmaza, 
# jelenleg így is vannak implementálva (szótárakkal). 
# Általános felhasználásra szánt programcsomagokat szervezhetük ún. csomagokba is, 
# melyek tetszőleges mélységű struktúrával rendelkezhetnek


#A modulok kiterjesztése .py a konvenciónak megfelelően. 
# Egy modul neve a modulon belül a __name__ modul-globális szimbólumon keresztül 
# hozzáférhető. Modulokat más scriptekből az 
# import vagy from module import * utasításokkal importálhatunk.





# This area is the global or module scope
number = 100
def outer_func():
     # This block is the local scope of outer_func()
     # It's also the enclosing scope of inner_func()
     def inner_func():
         # This block is the local scope of inner_func()
        print(number)

        def leg_inner_func():
            alma = 10

            def leg_leg_inner():
                alma = 120
            
            leg_leg_inner()
        leg_inner_func()
     print(inner_func.__name__)

     inner_func()

#outer_func()

a = 10
def outer_func():
     # This block is the local scope of outer_func()
     # It's also the enclosing scope of inner_func()
    a = 11
    def inner_func():        
        nonlocal a
        print(a)
        a = 12
         # This block is the local scope of inner_func()
        print(a)
    inner_func()
    print(a)

outer_func()
