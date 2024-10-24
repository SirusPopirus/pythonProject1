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


kilpa_autot = []

for i in range(1,11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    kilpa_autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu_jatkuu = True
while kilpailu_jatkuu:
    for auto in kilpa_autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)

        auto.kulje(1)

    for auto in kilpa_autot:
        if auto.kuljettu_matka >= 10000:
            kilpailu_jatkuu = False
            print(f"Auto {auto.rekisteritunnus} voitti!")
            break

print(f"{'Rekisteritunnus ':<15}{'Huippunopeus (km/h)':<20}{'Nopeus (km/h)':<20}{'Kuljettu matka (km)':<20}")
print("-" * 75)
for auto in kilpa_autot:
    print(f"{auto.rekisteritunnus:<15}{auto.huippunopeus:<20}{auto.tamanhetkinen_nopeus:<20}{auto.kuljettu_matka:<20.2f}")