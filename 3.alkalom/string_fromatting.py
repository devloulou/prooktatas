name = 'Lajos'

print("Lajos király")

# 1

# % -s os helyettesítés

print("% a király" %name)
print("%s a király" %name)

szam1 = 1
szam2=3

print("{szazalekjel} a {szam1:04X} király {szam2} {szam2} {szam2} {szam5}".format(szazalekjel=name, szam2=10, szam5=11, szam1=300))


b = 2

print("%f szám" %b)


# 2 - formatting
format_szoveg = ["Ricsi", "Karcsi"]

formazott_szoveg = "format_szoveg: {szoveg}".format(szoveg=format_szoveg)

print(formazott_szoveg)

str_ricsi = "ricsi"

print("format_szoveg: {szoveg}".format(szoveg=str_ricsi))
print("format_szoveg: {szoveg:s}".format(szoveg=str_ricsi)) # típus kényszerítés

# 3
my_list = ["adat", "adat"]
ms_str = "icsi"
my_string = f"my_list: {ms_str:s}" #kényszerített
my_string = f"my_list: {my_list}"

"" ''
print(f"{my_string}{['Ricsi', 'Karcsi']}{2}{tuple()}{print}")

# 4
from string import Template
lajos = "Lajos"
t = Template('$name a király')
t.substitute(name=lajos)
print(t.substitute(name=lajos))


str_rocs = f"{lajos} a király"

sql_string = """
select * from {tabla_neve}
"""

sql_string.format(tabla_neve = "dual")