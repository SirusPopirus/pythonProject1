pituus = float(input("Ilmoita kuhasi pituus senttimetreinä: "))
rep = 37 - pituus
if pituus >= 37:
    print("Hienoa, voit viedä kuhan kotiin.")

else:
    print(f"Laske kuhan takaisin järveen!\nKuha ei ole tarpeeksi pitkä, siitä puutuu {rep:.0f} cm")