# Tehtävä 7.2

nimet = set()

nimi = input("Anna nimi, tyhjä lopettaa: ")

while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
        nimet.add(nimi)

        nimi = input("Anna nimi, tyhjä lopettaa: ")

    else:
        print("Uusi nimi")
        nimet.add(nimi)

        nimi = input("Anna nimi, tyhjä lopettaa: ")


for nimi in nimet:
    print(nimi)