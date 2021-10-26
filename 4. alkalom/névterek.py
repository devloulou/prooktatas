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