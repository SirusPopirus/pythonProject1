rep = int(input("Syötä luku: "))
if rep == 2 or rep == 3 or rep == 5:
    print("Lukusi on alkuluku.")
elif rep % 2 == 0 or rep % 3 == 0 or rep % 5 == 0:
    print("Lukusi ei ole alkuluku.")
else:
    print("Lukusi on alkuluku.")