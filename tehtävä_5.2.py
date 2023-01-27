# Tehtävä 5.2

luvut = []

luku = input("Syötä luku (tyhjä lopettaa): ")
if luku !="":
    luku = int(luku)

while luku != "":
    luvut.append(luku)
    luku = input("Syötä luku (tyhjä lopettaa): ")
    if luku != "":
        luku = int(luku)

print("Antamasi numerot:")


for i in luvut:
    luvut.sort(reverse=True)

print(f'Viisi suurinta arvoa: {luvut[0:5]}')


