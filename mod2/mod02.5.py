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
kilo = kokomassa / 1000
kilo1 = int(kilo)
gramma = (kilo - kilo1) * 1000
print(f"Massa nykymittojen mukaan:\n {kilo1:.0f} kg ja {gramma:.2f} g")
