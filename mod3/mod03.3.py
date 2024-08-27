rep = input("Kerro sukupuolisi Nainen vai Mies: ")
rep1 = float(input("Kerro hemoglobiiniarvosi: "))

if rep == "Nainen" and 175>=rep1>=117:
    print("Hemoglobiiniarvosi on normaali")
elif rep == "Nainen" and 175<rep1:
    print("Hemoglobiiniarvosi on korkea")
elif rep == "Nainen" and rep1<117:
    print("Hemoglobiiniarvosi on alhainen")

if rep == "Mies" and 195>=rep1>=134:
    print("Hemoglobiiniarvosi on normaali")
elif rep == "Mies" and 195<rep1:
    print("Hemoglobiiniarvosi on korkea")
elif rep == "Mies" and rep1<134:
    print("Hemoglobiiniarvosi on alhainen")
else:
    print("Virheellinen sukupuoli")