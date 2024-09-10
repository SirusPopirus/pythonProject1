lentoasemat = {"EFHK":"Helsinki-Vantaa",
       "EFLP":"Lappeenranta",
       "EFMI":"Mikkeli",
       "EFTP":"Tampere-Pirkkala",
       "EFTU":"Turu",
       "EFPO":"Pori",
       "EFJY":"Jyväskylä",
       "EFKU":"Kuopio",
       "EFVA":"Vaasa",
       "EFKK":"Kokkola-Pietarsaari",
       "EFOU":"Oulu",
       "EFIV":"Ivalo",
       "EFKT":"Kittilä",
       "ESUP":"Pajala",
       "EFRO":"Rovaniemi",
       "EFKS":"Kuusamo"}
kek = input("Haluatko syöttää uuden lentoaseman (syötä: uusi),\nhakea lentoaseman tiedot (syötä: haku)\nvai haluatko lopettaa (syötä: lopeta): ")
while True:
    if kek == "uusi":
        rap = input("Syötä lentoaseman ICAO-koodi: ")
        rep = input("Syötä lentoaseman nimi: ")
        lentoasemat[rap] = rep
        kek = input(
        "Haluatko syöttää uuden lentoaseman (syötä: uusi),\nhakea lentoaseman tiedot (syötä: haku)\nvai haluatko lopettaa (syötä: lopeta): ")

    elif kek == "haku":
        teg = input("Syötä ICAO-koodi: ")
        if teg in lentoasemat:
            print(lentoasemat[teg])
        kek = input(
        "Haluatko syöttää uuden lentoaseman (syötä: uusi),\nhakea lentoaseman tiedot (syötä: haku)\nvai haluatko lopettaa (syötä: lopeta): ")

    elif kek == "lopeta":
        print("Ophjelma päättyi")
        break