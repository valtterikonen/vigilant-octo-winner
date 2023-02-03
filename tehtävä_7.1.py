# Tehtävä 7.1

vuodenajat = ("kevät", "kesä", "syksy", "talvi")

kkNro = int(input("anna kuukauden numero (1-12): "))

if (kkNro == 12 or kkNro == 1 or kkNro == 2):
    vuodenaika = vuodenajat[3]
elif (kkNro >= 3 and kkNro <= 5):
    vuodenaika = vuodenajat[0]

elif (kkNro >= 6 and kkNro <= 8):
    vuodenaika = vuodenajat[1]

elif (kkNro >= 9 and kkNro <= 11):
    vuodenaika = vuodenajat[2]

else:
    print("tuntematon")

print(f"{kkNro}. kuukausi kuuluu vuodenaikaan {vuodenaika}")