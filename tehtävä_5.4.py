# Tehtävä 5.4

toisto = 5
kaupungit = []

kaupunki = input("Syötä kaupunki: ")
kaupungit.append(kaupunki)

for i in kaupungit:
    kaupunki = input("Syötä kaupunki: ")
    kaupungit.append(kaupunki)

    toisto -= 1
    if toisto == 1:
        break

print()

for kaupunki in kaupungit:
    print(f"Nimeämäsi kaupungit: {kaupunki}")

