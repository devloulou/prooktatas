my_list = [
	{
		'foo':12,
		'bar':14
	},
	{
		'moo':52,
		'car':641
	},
	{
		'doo':6,
		'tar':84
	}
]

# 1. feladat: a fennt definiált my_list listából irassátok ki a kulcsokat és értékeket.
# A megoldás során törekedjetek a python list és dict műveletek használatára.

# 2.feladat:
# Írjatok egy olyan kis scriptet, ami teljesíti a következő feltételt:
# ha szam1 > szam2 akkor eredmeny = szam1 - szam2
# ha eredmeny > szam2 akkor eredmeny = szam2, különben eredmeny = 0

szam1 = 10
szam2 = 5
eredmeny = None

# 2. feladat, b: ha szam1 osztva szam2-vel 0 akkor az eredmény legyen szam2 négyzete: eredmeny = szam2^2

# 3. feladat: segítség: beépített típus ellenőrzés:               
#működő példa:
# a = "1"
# if type(a) == str:
#     print("a változó{valtozo} típusa string".format(valtozo=a))  


my_dict = {
            "auto": [{"type": "Volvo",
                     "color": "gold"
                    },
                    {"type": "Audi",
                     "color": "red"
                    },
                    {"type": "Reanult",
                     "color": "White"
                    } ],
            "driver": ["Heikki Kovalainen", "Bruno Senna", "Sebastien Buemi"],
            "licence": False,
            "age": 18
        }

# 3.1 feladat: az auto- hoz adjatok hozzá plusz 1 értéket, maradjanak meg a régi értékek is.
# a dictionary ezen kívül ne változzon.
# pl.
# "auto": [
#     {"type": "Volvo", 
#     "color": "gold"
#     },
#     {"type": "Audi",
#     "color": "red"
#     },
#     {"type": "Reanult",
#     "color": "White"
# },
# {"új kulcs": "új érték"}
#  ]

# 3.2 feladat: ha az age nagyobb mint 17, akkor a licence értéke legyen igaz.
# 3.3 feladat: Nem szeretjük a francia autót, töröljök a renault az autók közül. A többi érték ne változzon.
# 3.4 feladat: ha a dictionary valamelyik értéke lista, akkor azt az értéket alakítsuk át tuple-é.
# A típus vizsgálatot a példában megadott módon próbáljátok megoldani.

# 4. feladat: az alábbi változók segítségével állítsátok elő a következő stringet:
# Ágnes 20 éves és kedvenc hangszere a furulya.
# pluszpont: ha valaki 1-nél több megoldást ír

name = "Ágnes"
age = 20
hobby = "furulya"

# 5. feladat: merge-eljétek össze / egyesítsétek a két dictionary-t. A megoldás során törekedjetek
# valamilyen dict művelet / vagy egyéb máshol látott művelet használatával és manuális
# megadással létrehozni az új, egyesített dict-et
my_dict = {
            "szín": "kék",
            "árnyalat": "halvány"
        }

my_dict2 = {"auto": "Opel",
            "tipus": "Benzin"
            }


# 6.feladat: módosítsátok a listát úgy, hogy csak a print, a [], és None elemek maradjanak a listában.
# Törekedjetek a lista múveletek használatára

my_list = [1,2,3,47,8,9,5, print, [], None, 5,6,4,3,56]