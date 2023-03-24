# Tehtävä 11.2

class Auto:
    def __init__(self, rekisterinumero, huippunopeus):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.matkamittari = 0

    def aja(self, tuntimaara):
        self.matkamittari += tuntimaara * self.huippunopeus


class Sahkoauto(Auto):
    def __init__(self, rekisterinumero, huippunopeus, akkukapasiteetti):
        super().__init__(rekisterinumero, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def lataa(self):
        print("Akkua ladataan...")


class Polttomoottoriauto(Auto):
    def __init__(self, rekisterinumero, huippunopeus, bensatankin_koko):
        super().__init__(rekisterinumero, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

    def tankkaa(self):
        print("Bensaa tankataan...")

sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.huippunopeus = 160
polttomoottoriauto.huippunopeus = 170

sahkoauto.aja(3)
polttomoottoriauto.aja(3)

print("Sähköauton matkamittari:", sahkoauto.matkamittari)
print("Polttomoottoriauton matkamittari:", polttomoottoriauto.matkamittari)