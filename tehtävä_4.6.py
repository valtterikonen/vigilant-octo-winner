# Tehtävä 4.6

N = 1000000

import random

x = random.uniform(-1, 1)
y = random.uniform(-1, 1)
print(f"Arvottu piste: {x}, {y}")
if x + x + y + y < 1:
    print("Piste on ympyrän sisällä")

else:
    print("Piste ei ole ympyrän sisällä")

