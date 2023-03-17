# Tehtävä 9.3

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 60
        self.matka = 2000

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tuntimäärä):
        self.matka += self.nopeus * tuntimäärä

    def __str__(self):
        return f'Auton rekisteritunnus: {self.rekisteritunnus}, huippunopeus: {self.huippunopeus} km/h, nopeus: {self.nopeus} km/h, matka: {self.matka} km'

auto = Auto("ABC-123", 142)
print()
print("Kulje")
auto.kulje(1.5)
print(auto)