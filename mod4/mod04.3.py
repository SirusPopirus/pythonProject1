numbers = []

while True:
    rep = (input("Syötä luku: "))

    if rep == "":
        break

    numbers.append(float(rep))

if numbers:
    print("Pienin luku on: ", min(numbers))
    print("Suurin luku on: ", max(numbers))
