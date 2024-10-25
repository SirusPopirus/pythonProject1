class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.ylin_kerros or kohde_kerros < self.alin_kerros:
            print(f"Kerrosta {kohde_kerros} ei ole olemassa!")
            return
        if self.nykyinen_kerros < kohde_kerros:
            while self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylos()
        elif self.nykyinen_kerros > kohde_kerros:
            while self.nykyinen_kerros > kohde_kerros:
                self.kerros_alas()

    def kerros_ylos(self):
        if self.nykyinen_kerros == self.ylin_kerros:
            print("Suurin kerros on jo saavutettu!")
            return
        self.nykyinen_kerros += 1
        print(f"Nykyinen kerros {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros == self.alin_kerros:
            return
        self.nykyinen_kerros -= 1
        print(f"Nykyinen kerros {self.nykyinen_kerros}")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        self.luo_hissi(lkm)

    def luo_hissi(self, lkm):
        for nro in range(lkm):
            uusi_hissi = Hissi(self.alin_kerros, self.ylin_kerros)
            self.hissit.append(uusi_hissi)

    def aja_hissia(self,hissi_nro, tavoitekerros):
        ajettava_hissi = self.hissit[hissi_nro - 1]
        ajettava_hissi.siirry_kerrokseen(tavoitekerros)
        print("-- Hissi on perillä")

    def palohalytys(self):
        for i in range(len(self.hissit)):
            self.aja_hissia(i, self.alin_kerros)


taloA = Talo(1, 7, 3)
taloA.aja_hissia(1, 5)
taloA.aja_hissia(2, 3)
taloA.aja_hissia(3, 7)
taloA.palohalytys()