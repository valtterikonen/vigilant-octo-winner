# Tehtävä 4.2

tuuma = int(input("Syötä tuumamäärä: "))

cm = float(tuuma * 2.54)

while tuuma >= 0:
    cm = float(tuuma * 2.54)
    print(tuuma, "tuumaa on" , cm, "senttimetriä")
    print()
    tuuma = int(input("Anna uusi luku tuumina: "))
    print()
print()
print("Toiminnot lopetettu")


