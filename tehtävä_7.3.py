# Tehtävä 7.3

lentoasemat = {"Helsinki-Vantaan lentoasema": "EFHK", "Pirkkalan lentoasema": "PIRK", "Porin lentoasema": "POR"}

def lisaa():
    tunnus = input("Anna lentoaseman tunnus: ")
    nimi = input("Anna lentoaseman nimi: ")
    lentoasemat[tunnus]=nimi
    return

def hae():
    tunnus = input("Anna lentoaseman tunnus: ")
    if tunnus in lentoasemat:
        print(f'{lentoasemat[tunnus]}')
    return

def tulosta():
    for asema in lentoasemat:
        print(f"{lentoasemat, asema}")
    return


toiminto = -1

while toiminto != 3:
    print("0 = tulosta lentoasemien tiedot")
    print("1 = lisää uusi lentoasema")
    print("2 = hae lentoasema")
    print("3 = lopeta")

    toiminto = int(input("Valitse toiminto: "))
    if toiminto == 0:
        tulosta()
    elif toiminto == 1:
        lisaa()
    elif toiminto == 2:
        hae()

print("Kiitos ja näkemiin")