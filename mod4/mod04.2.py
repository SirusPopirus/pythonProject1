rep = float(input("Syötä tuuma määrä: ")) * 2.54
while rep:
    if rep < 0:
        print("Syötetty negatiivinen tuuma määrä")
        break

    elif rep > 0:
        print(f"{rep} cm")
        rep = float(input("Syötä tuuma määrä: ")) * 2.54