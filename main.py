import requests
import json
import citySetter

URL = "https://trouverunlogement.lescrous.fr/api/fr/search/27"
f = open("headers.json")
city = input("Entrez votre ville : ")
data = citySetter.get_city_info(city)

head = {
    'Accept': '*/*',
    'User-Agent': 'Thunder Client (https://www.thunderclient.com)'
}
src = requests.post(URL, json=data, headers=head).text

data = json.loads(src)

nb_logements = data["results"]["total"]

data = data["aggregations"]["markers"]

if not data:
    print("Pas de logements disponible ")

else:
    print("Les logements disponible a " + city)
    for ele in data:
        arr = ele["residences"]
        for res in arr:
            print(res["label"])
