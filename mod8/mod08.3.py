from geopy import distance
import mysql.connector


conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='matveib',
    password='salasana',
    autocommit=True,
    collation='utf8mb4_general_ci'
)


def hae_kordinaatit(rep):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{rep}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result


rep1 = input("Syötä 1. Lentoaseman ICAO-koodi: ").upper()
rep2 = input("Syötä 2. Lentoaseman ICAO-koodi: ").upper()


kordinaatit1 = hae_kordinaatit(rep1)
kordinaatit2 = hae_kordinaatit(rep2)


if kordinaatit1 and kordinaatit2:

    etaisyys = distance.distance(kordinaatit1, kordinaatit2).km
    print(f"Etäisyys lentokenttien välillä on {etaisyys:.2f} kilometriä.")
else:
    print("Jomman kumman lentokentän koordinaatteja ei löytynyt.")