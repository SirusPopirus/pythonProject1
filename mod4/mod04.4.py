import random
luku = int(input("Syötä luku 1-10: "))
rep = random.randint(1, 10)
while luku:
      if luku < rep:
            print("Liian pieni arvaus: ")
            luku = int(input("Syötä luku 1-10: "))
      elif luku > rep:
            print("Liian suuri arvaus: ")
            luku = int(input("Syötä luku 1-10: "))
      elif luku == rep:
            print("Oikein")
            break