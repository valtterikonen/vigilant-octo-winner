# Tehtävä 4.5

user = input("Syötä käyttäjätunnus: ")
password = input("Syötä salasana: ")

toisto = 5

while user == "python":
    password = "rules"
    print("Tervetuloa")
    break

while user != "python":
    password != "rules"
    print("Pääsy evätty")

    user = input("Syötä käyttäjätunnus: ")
    password = input("Syötä salasana: ")

    toisto -=1
    if toisto == 1:
        break



