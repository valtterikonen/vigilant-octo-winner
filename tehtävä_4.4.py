# Tehtävä 4.4

luku = int(input("Syötä arvaus: "))

import random

x = random.uniform(0, 10)

while luku == x:
    print("Oikein")

while luku > x:
    print("Liian suuri arvaus")
    luku = int(input("Syötä arvaus: "))

while luku < x:
    print("Liian pieni arvaus")
    luku = int(input("Syötä arvaus: "))
