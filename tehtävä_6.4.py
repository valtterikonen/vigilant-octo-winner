# Tehtävä 6.4

def summaa(lista):
    summa = 0
    for n in lista:
        summa += n
    return summa

luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9]

tulos = summaa(luvut)
print(f'Listan lukujen summa: {tulos}')

