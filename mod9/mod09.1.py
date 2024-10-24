class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkellinen_nopeus = 0
        self.kuljettu_matka = 0

uusi_auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus: {uusi_auto.rekisteritunnus}")
print(f"Auton huippunopeus: {uusi_auto.huippunopeus} km/h")
print(f"Auton tämänhetkinen nopeus: {uusi_auto.tamanhetkellinen_nopeus} km/h")
print(f"Auton kuljettu matka: {uusi_auto.kuljettu_matka}")