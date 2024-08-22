command = input("Syötä kanta: ")
command2 = input("Syötä korkeus: ")
pituus = float(command)
leveys = float(command2)
piiri = pituus * 2 + leveys * 2
pintaala = pituus * leveys
print("Suorakulmion piiri on: " + str(piiri))
print("Suorakulmion pinta-ala on: " + str(pintaala))

