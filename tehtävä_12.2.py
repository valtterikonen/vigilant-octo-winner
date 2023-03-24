# Tehtävä 12.2

import json
import requests

hakusana = input("Syötä kaupunki: ")

pyyntö = "https://api.openweathermap.org/data/2.5/weather?q=" + hakusana + "&appid=6d899e157067e600384415b0dc8b5dbd&units=metric"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()

        print()
        print(f"Temperature: {json_vastaus['main']['temp']} celsius")
        print(f"Weather: {json_vastaus['weather'][0]['description']}")

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")