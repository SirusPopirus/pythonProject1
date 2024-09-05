rep = []
kys = input("Syötä lukuja tai paina enter lopettaakseen: ")
while kys != "":
    rep.append(int(kys))
    kys = input("Syötä lukuja tai paina enter lopettaakseen: ")
rep.sort(reverse=True)
print(rep[:5])