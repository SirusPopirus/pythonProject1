import requests

def hae_chuck_norris_vitsi():
    try:
        vastaus = requests.get("https://api.chucknorris.io/jokes/random")
        if vastaus.status_code == 200:

            data = vastaus.json()

            print(data['value'])
        else:
            print("Virhe haettaessa vitsiä. Yritä uudelleen myöhemmin.")
    except Exception as e:
        print(f"Tapahtui virhe: {e}")

hae_chuck_norris_vitsi()
