import requests
import json

URL = "https://trouverunlogement.lescrous.fr/api/fr/search/27"  
f = open("headers.json")
data = json.load(f)

head = {
    'Accept': '*/*',
    'User-Agent': 'Thunder Client (https://www.thunderclient.com)'
}
# print(f.read())
src = requests.post(URL, json=data, headers=head).text

data  = json.loads(src)

nb_logements = data["results"]["total"]

data = data["aggregations"]["markers"]

print(str(nb_logements) + " Logement(s) sont disponible(s) ")
for ele in data:
    arr = ele["residences"]
    for res in arr:
        print(res["label"])


