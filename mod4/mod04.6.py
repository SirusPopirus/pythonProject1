# piin likiarvon laskeminen
# π≈4n/N. jossa n on yksikköympyrän sisälle osuvat pisteet, N on kaikki pisteet
# epäyhtälöllä x^2+y^2<1 testataan, onko yksittäinen piste ympyrän sisällä

#from random import randint
#randint(-1,1)
import math
import random
N = int(input("Monta pistettä haluat? "))
iterator = 0
#TODO: Kysy N arvo käyttäjältä
n = 0 # ympyrään sisään osuvat pisteet
while iterator < N:
    #arvotaan kordinaatit väliltä -1 ja 1
    iterator += 1
    x = random.random() * 2 - 1
    y = random.uniform(-1, 1)
    print(f"Satunnainen piste: {x}, {y}")
    if x**2 + y**2 < 1:
        print("Osui ympyrän sisälle.")
        n = n + 1
print(f"{N} pisteestä {n} osui yksikköympyrän sisälle.")
result = 4 * n/N
print(f"Piin likiarvo on {result}")
print (f"Virhe {result- math.pi}")