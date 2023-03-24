# Tehtävä 10.2

class Hissi:

    def __init__(self, ylin, alin):
        self.ylin = ylin
        self.alin = alin
        self.kerros = alin

    def kerros_ylös(self):
        self.kerros = self.kerros + 1
        print(f'Hissi on kerroksessa {self.kerros}')


    def kerros_alas(self):
        self.kerros = self.kerros - 1
        print(f'Hissi on kerroksessa {self.kerros}')


    def siirry_kerrokseen(self, uusi_kerros):
        while uusi_kerros > self.kerros:
            self.kerros_ylös()
        while uusi_kerros < self.kerros:
            self.kerros_alas()


h = Hissi(5,0)
h.siirry_kerrokseen(5)
print()
h.siirry_kerrokseen(0)

class Talo:
    def __init__(self, ylinkrs: int, alinkrs: int, hissit: int):
        # Tehdään talolle hissit
        self.ylinkrs = ylinkrs
        self.alinkrs = alinkrs
        self.hissilista = []
        for n in range(hissit):
            uusihissi = Hissi(ylinkrs, alinkrs)
            self.hissilista.append(uusihissi)

    def aja_hissiä(self, hissinro: int, kohdekerros: int):
        print(f"Siirretään hissi {hissinro} kerrokseen {kohdekerros}")
        self.hissilista[hissinro-1].siirry_kerrokseen(kohdekerros)

talo = Talo(5,1,2)
print()
talo.aja_hissiä(2,3)
