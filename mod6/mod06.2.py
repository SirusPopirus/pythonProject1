import random
kak = int(input("Kirjoita monta tahkoa haluat nopalle: "))

def luku():
    return random.randint(1, kak)
def noppa():
    rep = 0
    while rep != kak:
        rep = luku()
        print(f"{rep}")
noppa()