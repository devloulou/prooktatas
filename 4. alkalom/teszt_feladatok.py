# 1. feladat:
# a my_list2 listába helyezzük át a az utolsó 4 elemet a my_list listából
# Törekedjetek az tanult megoldások használatára

my_list = ["alma", "Géza", int, 1, 2, 3, 4, 5]
my_list2 = []

my_list2 = my_list[-4:]

#print(my_list2)


# 2. feladat: a my_list litában lévő duplikációkat szüntessük meg.
# Törekedjetek a tanult megoldások használatára
my_list = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6]

my_list = list(set(my_list))
# print(list(set(my_list)))
# print(my_list)

# 3. feladat: Adjatok egy új állás-t az állások-hoz. 
# Kérlek, hogy ne ciklussal oldjátok meg a feladatot, hanem dict műveletekkel, manuálisan

# A feladat megoldása során törekedjetek a dictionary / egyéb műveletek használatára.
# Maga a dict struktúrája ne változzon.
my_dict = {
       "állások": { 
           "Profession.hu": {
                                "pozíció": "Fejlesztő",
                                "fizetés": "600000",
                                "cég": "Vodafone"
                            }, 
            "NoFluffJobs": {
                                "pozíció": "Üzemeltető",
                                "fizetés": 500000,
                                "cég": "Telekom"
                            }, 
            "Linkedin": {
                                "pozíció": "Team leader",
                                "fizetés": "1600000",
                                "cég": "Erisscon"
                            } , 
            "Egyéb": {
                                "pozíció": "Kéményseprő",
                                "fizetés": "300000",
                                "cég": "FKF"
                            }  
        
        }

}

# my_dict['állások'].update({"saját": {
#                                 "pozíció": "Fejlesztő",
#                                 "fizetés": "600000",
#                                 "cég": "Ricsi"
#                             }})

my_dict['állások']['saját'] ={
                                "pozíció": "Fejlesztő",
                                "fizetés": "600000",
                                "cég": "Ricsi"
                            }


#print(my_dict)

# 3.1 feladat: Töröljétek az Egyéb hirdetést. A többi állás változatlan maradjon.

my_dict['állások'].pop("Egyéb")

#print(my_dict)

# 3.2 feladat: Ahol a fizetés string, ott a fizetés legyen szám típusú. Kérlek, hogy ne ciklussal
# oldjátok meg, hanem manuálisan. Vezérlő szerkezetet használhattok (de nem szükséges).

my_dict['állások']["Profession.hu"]["fizetés"] = int(my_dict['állások']["Profession.hu"]["fizetés"])

# print(my_dict)
# print()

# 4. feladat: a my_list-ben megadott elemeket bontsuk ki, és egy listában legyenek az elemek
# pl: lista[1,2,3,4,5,6,7,8,9]
my_list = [[1,2,3],[4,5,6],[7,8,9]]

#my_list = [*my_list[0], *my_list[1], *my_list[2]]

my_list2 = my_list[0] + my_list[1] + my_list[2]
# print(my_list)
# print(my_list2)


# 5. feladat: a my_tuple változóban lévő adatokban vannak Error-al kezdődő értékek.
# Az eddig tanultak  használatával oldjuk meg, hogy az Error-al kezdődő értékek ne szerepeljenek a tuple-ben.
# Kérlek, hogy ne használjatok ciklusokat.
# Megoldási metodika nyugodtan legyen manuális.
# A végén a my_tuple = ("12", "14") eredményt szeretném látni.

my_tuple = ("Error in line 99", "12", "14", "Error in line 45")

my_tuple2 = tuple(my_tuple[1:-1])

print(my_tuple2)