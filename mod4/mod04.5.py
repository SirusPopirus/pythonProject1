tunnus = input("Syötä käyttäjätunnus: ")
sala = input("Syötä salasana: ")
vaarat = 0
while vaarat < 4:

    if tunnus == "python" and sala == "rules":
        print("Tervetuloa")
        break

    elif tunnus != "python" or sala != "rules":
        print("Väärä tunnus tai salasana")
        tunnus = input("Syötä käyttäjätunnus: ")
        sala = input("Syötä salasana: ")
        vaarat = vaarat + 1
print("Pääsy evätty")