command = input("Syötä massa leivisköinä: ")
command1 = input("Syötä massa nauloina: ")
command2 = input("Syötä massa luoteina: ")
leiviskä = float(command)
naula = float(command1)
luoti = float(command2)
lemassa = leiviskä * 20
namassa = naula * 32
lumassa = luoti * 13.3
kokomassa =(lemassa * 32) * 13.3 + (namassa * 13.3) + lumassa
print(f"Massa nykymittojen mukaan: " + str(kokomassa))
