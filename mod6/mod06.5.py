def lista(luku):
    return [i for i in luku if i % 2 == 0]

def kak():
    luku_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parillinen = lista(luku_lista)
    print(luku_lista)
    print(parillinen)
kak()