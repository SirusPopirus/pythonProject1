import requests

def hae_sää(kaupunki):
    pyyntö = (f"https://api.openweathermap.org"
              f"/data/2.5/weather?q={kaupunki}&"
              f"appid=259fbb404512322b82e7a1e012bb912f&units=metric&lang=fi")
    r = requests.get(pyyntö).json()
    weather = r["weather"][0]["description"]
    temperature = r["main"]["temp"]
    print(weather)
    print(f"Lämpötila on {temperature:.1f} astetta")

kaupunki = input("Kaupunki: ")
hae_sää(kaupunki)