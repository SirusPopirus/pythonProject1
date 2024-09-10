nimet = set()
kek = input("Syötä nimi: ")
while kek:
    if kek not in nimet:
        nimet.add(kek)
        print("Uusi nimi")
        kek = input("Syötä nimi: ")
    elif kek in nimet:
        print("Aiemmin syötetty nimi")
        kek = input("Syötä nimi: ")
for kek in nimet:
    print(kek)