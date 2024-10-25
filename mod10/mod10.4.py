import random

class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos

        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
        else:
            self.tamanhetkinen_nopeus = uusi_nopeus

    def kulje(self, tunnit):
        uudet_tunnit = self.tamanhetkinen_nopeus * tunnit
        self.kuljettu_matka = self.kuljettu_matka + uudet_tunnit


class Kilpailu:
    def __init__(self, kilpailu_nimi, km_pituus, osallistujat):
        self.kilpailu_nimi = kilpailu_nimi
        self.km_pituus = km_pituus
        self.osallistujat = osallistujat

    def tunti_kuluu(self):
        for auto in self.osallistujat:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteritunnus ':<15}{'Huippunopeus (km/h)':<20}{'Nopeus (km/h)':<20}{'Kuljettu matka (km)':<20}")
        print("-" * 75)
        for auto in self.osallistujat:
            print(f"{auto.rekisteritunnus:<15}{auto.huippunopeus:<20}{auto.tamanhetkinen_nopeus:<20}{auto.kuljettu_matka:<20.2f}")

    def kilpailu_ohi(self):
        kilpailu_loppu = False
        for auto in self.osallistujat:
            if auto.kuljettu_matka >= self.km_pituus:
                kilpailu_loppu = True
        return kilpailu_loppu

kilpa_autot = []

for i in range(1,11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    kilpa_autot.append(Auto(rekisteritunnus, huippunopeus))

uusi_kilpailu = Kilpailu("Suuri romuralli", 8000, kilpa_autot)

kesto = 0
kilpailu_end = False
while not kilpailu_end:
    uusi_kilpailu.tunti_kuluu()
    kesto = kesto + 1
    if kesto % 10 == 0:
        print(f"Kilpailu kesti {kesto} tuntia.")
        uusi_kilpailu.tulosta_tilanne()
    kilpailu_end = uusi_kilpailu.kilpailu_ohi()
print("Kilpailu on päättynyt!")
print(f"Kilpailu kokonais kesto on {kesto} tuntia.")
uusi_kilpailu.tulosta_tilanne()