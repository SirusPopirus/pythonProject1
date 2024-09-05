from random import randint

dot = 0
kys = int(input("Montako arpakuutiota heität: "))
for i in range(kys):
    rep = randint(1, 6)
    dot = dot + rep
print(dot)