kak = float(input("Syötä nastegallonojen määrän: "))
def galon():
    litrs = kak * 3.785
    print("Se on: " + str(litrs) + " litraa.")
    return litrs
while kak >= 0:
    galon()
    kak = float(input("Syötä nastegallonojen määrän: "))
    if kak <= 0:
        break