# Tehtävä 4.3

pienin = suurin = 0

lukustr = int(input("Anna kokonaisluku (tyhjä lopettaa): "))

if lukustr != "":
    pienin = suurin = int(lukustr)

while lukustr != "":
    luku = int(lukustr)

    if luku > suurin:
        suurin = luku

    lukustr = input("Anna kokonaisluku (tyhjä lopettaa): ")

if lukustr == "":
    print(f'Suurin luku: {suurin}, Pienin luku: {pienin}')

