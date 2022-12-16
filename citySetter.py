from geopy.geocoders import Nominatim
import json

geolocator = Nominatim(user_agent='myapplication')


def get_city_info(city):
    location = geolocator.geocode(city)

    data = location.raw.get("boundingbox")

    lat1 = float(data[1])

    lat2 = float(data[0])

    long1 = float(data[3])

    long2 = float(data[2])

    with open("headers.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["location"] = [{'lon': round(long2, 4), 'lat': round(lat1, 2)}, {'lon': round(long1, 4), 'lat': round(lat2, 4)}]

    return data
