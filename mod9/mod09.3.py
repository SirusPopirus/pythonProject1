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



uusi_auto = Auto("ABC-123", 142)

uusi_auto.kiihdyta(100)
print(f"Auton nopeus on {uusi_auto.tamanhetkinen_nopeus} km/h")
uusi_auto.kuljettu_matka = 2000
print(f"Auto on kulkenut {uusi_auto.kuljettu_matka} km")
uusi_auto.kulje(1.5)
print(f"Autolla kuljettu matka 1.5 tunnin jälkeen {uusi_auto.kuljettu_matka} m")