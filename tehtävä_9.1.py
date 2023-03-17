# Tehtävä 9.1

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
    pass

auto = Auto("ABC-123", 142)

print(f'Auton rekisteritunnus:{auto.rekisteritunnus:s}, huippunopeus: {auto.huippunopeus:d}km/h.')
print(f'Auton nopeus tällä hetkellä {auto.nopeus}, kuljettu matka: {auto.matka}.')










