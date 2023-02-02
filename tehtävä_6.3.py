# Tehtävä 6.3


gallona = int(input("Syötä gallonamäärä: "))


def muutos(gallona):
    litra = 3.785 * gallona
    return litra

tulos = muutos(gallona)

while tulos > 0:
    print(f'Gallonaa {gallona} litroina {tulos}')
    gallona = float(input("Syötä gallonamäärä: "))
    tulos = muutos(gallona)

print("Syötetty määrä negatiivinen")
