import random


def luku():
    return random.randint(1,6)
def noppa():
    rep = 0
    while rep != 6:
        rep = luku()
        print(f"{rep}")
noppa()