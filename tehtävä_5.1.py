# Tehtävä 5.1

import random

noppa = int(input("Syötä noppien lukumäärä: "))
noppa_summa = 0

for i in range(noppa):
    toisto = random.randint(1, 6)
    noppa_summa += toisto

print("Noppien silmälukujen summa:", noppa_summa)


