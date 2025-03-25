import requests


def euro():
    response = requests.get("https://cbu.uz/oz/arkhiv-kursov-valyut/json/")
    data = response.json()[1]['Rate']
    return float(data)
