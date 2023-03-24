# Tehtävä 12.1

import json
import requests


pyyntö = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(pyyntö).json()


print(json.dumps(vastaus["value"]))

