# Tehtävä 6.2

import random

tahko = int(input("Syötä noppien lukumäärä: "))


def heitto(tahko):
    return random.randint(1, tahko)


result = 0
while result < tahko:
    result = heitto(tahko)
    print(f'Tahko silmäluku: {result}')

if result == tahko:
    print("Maksimi silmäluku!")
