# raise Exception()
# assert

# try:
# except:

# kivételgenerálás - saját kivételgenerálás
def my_func(szam1, szam2):
    if szam1 > szam2:
        osszeg = szam1 + szam2
    else:
        #raise Exception("Szam1 nem nagyobb mint a szam2")
        raise Exception(ValueError)

    return osszeg


osszeg = my_func(4,3)

#print(osszeg)

#osszeg = my_func(3, 4)


def my_func2(szam1, szam2):
    assert(szam1<szam2 or szam2 == 0) , 'hülye vagyok'
    if szam1 > szam2:
        osszeg = szam1 + szam2
    else:
        if szam2 == 0:
        #raise Exception("Szam1 nem nagyobb mint a szam2")
            raise Exception(ValueError)
        else:
            assert(szam1 > szam2), 'hülye vagyok'
            osszeg = szam1 + szam2

    return osszeg

# test = my_func2(0, -1)

# print(test)

# kivételkezelés
def kiir(szam1, szoveg):
    osszeg = 100
    try:
        osszeg = szam1 + szoveg        
    except Exception as barmit_irhatok_ide:
        print(barmit_irhatok_ide)

    return osszeg

alma = kiir(10, [])

print(alma)