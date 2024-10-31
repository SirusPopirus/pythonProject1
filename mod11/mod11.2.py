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
        uudet_kilometrit = self.tamanhetkinen_nopeus * tunnit
        self.kuljettu_matka += uudet_kilometrit

# Aliluokka Sähköauto
class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

# Aliluokka Polttomoottoriauto
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki_koko = bensatankki_koko

# Pääohjelma
sahkoauto = Sahkoauto("ABC-15", 180, 52.5)  # Rekisteritunnus, huippunopeus, akkukapasiteetti
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)  # Rekisteritunnus, huippunopeus, bensatankki_koko

# Asetetaan nopeudet
sahkoauto.kiihdyta(150)
polttomoottoriauto.kiihdyta(100)

# Käsketään autoja ajamaan kolmen tunnin ajan
sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

# Tulostetaan autojen matkamittarilukemat
print(f"{'Rekisteritunnus':<15}{'Kuljettu matka (km)':<20}")
print("-" * 35)
print(f"{sahkoauto.rekisteritunnus:<15}{sahkoauto.kuljettu_matka:<20.2f}")
print(f"{polttomoottoriauto.rekisteritunnus:<15}{polttomoottoriauto.kuljettu_matka:<20.2f}")
