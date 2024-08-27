number = int(input("Kerro vuosiluku: "))

if number % 400 == 0:
    print("Vuosi on karkausvuosi")

elif number % 100 == 0:
    print("Vuosi ei ole karkausvuosi")

elif number % 4 == 0:
    print("Vuosi on karkausvuosi")

else:
    print("Vuosi ei ole karkausvuosi")