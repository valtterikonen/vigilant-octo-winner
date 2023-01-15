# Tehtävä 2.5

le_str = input("Anna leiviskät: ")
na_str = input("Anna naulat: ")
lu_str = input("Anna luodit: ")

import math

le = float(le_str)
na = float(na_str)
lu = float(lu_str)

luodit = lu*(13.3)
naulat = na*(13.3*32)
leiviskät = le*(425.6*20)

grammat = luodit+naulat+leiviskät
kilot = math.floor(grammat/1000)

print("Massa kiloissa ja grammoissa: ")
print(kilot, "kiloa ja ", round(grammat-kilot/1000, 1), "grammaa.")