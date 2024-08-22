import math

command = input("Syötä säde: ")
säde = float(command)
pintaala = säde **2 * math.pi
print("Ympyrän pinta-ala on: " + str(pintaala))
