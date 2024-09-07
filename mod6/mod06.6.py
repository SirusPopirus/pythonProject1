import math
def calc(rep, hint):
    rep = rep / 1000
    r = rep/2
    ar = math.pi * r ** 2
    return hint/ar

halk = float(input("Syötä 1. pizzan halkaisija (cm): "))
halk2 = float(input("Syötä 2. pizzan halkaisija (cm): "))
maks1 = float(input("Syötä 1. pizzan hinta: "))
maks2 = float(input("Syötä 2. pizzan hinta: "))

nelihint = calc(halk, maks1)
nelihint1 = calc(halk2, maks2)

print(f"Ensimmäisen pizzan neliö hinta on {nelihint:.2f}")
print(f"Toisen pizzan neliö hinta on {nelihint1:.2f}")

if nelihint < nelihint1:
    print("Eka pizza on neliöhintaan halvempi")

elif nelihint > nelihint1:
    print("Toinen pizza on nelihintaan halvempi")
else:
    print("Pizzojen neliöhinta on sama")