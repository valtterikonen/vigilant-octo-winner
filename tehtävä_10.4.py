# Tehtävä 10.4

import random

class Auto:
    def __init__(self, tunnus, huippu, nopeusatm=0, matka=0):
        self.tunnus = tunnus
        self.huippu = huippu
        self.nopeusatm = nopeusatm
        self.matka = matka

    def kiihdytä(self, nopeuden_muutos):
        self.nopeusatm += nopeuden_muutos
        if self.nopeusatm >= self.huippu:
            self.nopeusatm = self.huippu
        if self.nopeusatm <= 0:
            self.nopeusatm = 0

    def kulje(self, tunnit, tulostus):
        self.matka += tunnit * self.nopeusatm
        if tulostus == True:
            print(f"Auto on kulkenut {self.matka} km.")


    def tiedot(self):
        print(f"Auton, jonka rekisterinumero on {self.tunnus:s}, huippunopeus on {self.huippu:d} km/h.")
        print(f"Auton nopeus tällä hetkellä on {self.nopeusatm:d} km/h ja kuljettu matka {self.matka:d} km.")


autot = []
for i in range(1, 11):
    auto = Auto(f"ABC-{i}", random.randint(100, 200))
    autot.append(auto)

pelijatkuu = True
kierros = 1
while pelijatkuu:
    for i in autot:
        i.kiihdytä(random.randint(-10, 15))
        i.kulje(1, False)
        if i.matka >= 10000:
            print(f"Auto {i.tunnus} on ajanut ensimmäisenä 10 000 kilometriä!")
            print()
            pelijatkuu = False
            break

for i in autot:
    print(f"Auton {i.tunnus} tiedot:   huippunopeus: {i.huippu}km/h,   "
          f"nopeus pelin lopussa: {i.nopeusatm}km/h,   kuljettu matka: {i.matka} kilometriä")

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        times = 0
        for auto in autot:
            auto = autot(times)
            auto.kiihdytä(random.randint(-10,15))
            auto.kulje(1)
            times += 1

    def tulosta_tilanne (self):
        times = 0
        for auto in autot:
            auto = autot[times]
            auto.tiedot()
            times += 1

    def kilpailu_ohi(self):
        kilpailu_ohi = False
        for auto in autot:
            if auto-matka >= self.pituus:
                kilpailu_ohi = True
                print(f' Auto {auto.tunnus} on ajanut ensimmäisenä {self.pituus} kilometriä')
                if kilpailu_ohi:
                    break
        return kilpailu_ohi