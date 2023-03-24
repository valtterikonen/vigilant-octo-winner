# Tehtävä 10.1

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






