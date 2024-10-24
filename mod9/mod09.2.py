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


uusi_auto = Auto("ABC-123", 142)
print(f"Auton alkunopeus on: {uusi_auto.tamanhetkinen_nopeus}")
uusi_auto.kiihdyta(30)
print(f"Nopeus kiihdyttyä (+30km/h): {uusi_auto.tamanhetkinen_nopeus}")
uusi_auto.kiihdyta(70)
print(f"Nopeus kiihdyttyä (+70km/h): {uusi_auto.tamanhetkinen_nopeus}")
uusi_auto.kiihdyta(50)
print(f"Nopeus kiihdyttyä (+50km/h): {uusi_auto.tamanhetkinen_nopeus}")
uusi_auto.kiihdyta(-200)
print(f"Nopeus hätäjarrutuksen jälkeen (-200km/h): {uusi_auto.tamanhetkinen_nopeus}")
