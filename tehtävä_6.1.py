# Tehtävä 6.1

import random

def heitto()
    return random.randint(1,6)

result = 0
while result != 6:
    result = heitto()
    print(f'Arpakuution tulos: {result}')


