command = input("Syötä kokonaisluku: ")
command2 = input("Syötä toinen kokonaisluku: ")
command3 = input("Syötä kolmas kokonaisluku: ")
luku1 = int(command)
luku2 = int(command2)
luku3 = int(command3)
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3
print("Lukujen summa on: " + str(summa))
print("Lukujen tulo on: " + str(tulo))
print("Lukujen keskiarvo on: " + str(keskiarvo))
