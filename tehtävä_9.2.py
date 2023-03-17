# Tehtävä 9.2

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def __str__(self):
        return f'Auton rekisteritunnus: {self.rekisteritunnus}, huippunopeus: {self.huippunopeus} km/h, nopeus: {self.nopeus} km/h, matka: {self.matka} km'

auto = Auto("ABC-123", 142)
print(auto)
print()
print("Kiihdytys")
auto.kiihdytä(30)
print(auto)
auto.kiihdytä(70)
print(auto)
auto.kiihdytä(50)
print(auto)
print()
print("Jarrutus")
auto.kiihdytä(-200)
print(auto)