# Tehtävä 6.5

def fixed(lista):
    parilliset = []
    for n in lista:
        if n%2==0:
            parilliset.append(n)
    return parilliset

luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9]


tulos = fixed(luvut)


print(f'Listan luvut: {luvut}')
print(f'Listan parilliset luvut: {tulos}')

