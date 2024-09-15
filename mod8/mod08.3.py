from geopy import distance
import mysql.connector
conn = mysql.connector.connect(
host= '127.0.0.1',
    port= 3306,
    database= 'flight_game',
    user= 'root',
    password= '<PASSWORD>',
    autocommit=True,
    collation= 'utf8mb4_general_ci'
    )
def hae_kordinaatit(rep):
    sql = f"SELECT latitude_deg, longtitude_deg FROM airport WHERE ident = '{rep}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

rep1 = input("Syötä 1. Lentoaseman ICAO-koodi: ").upper()
rep2 = input("Syötä 2. Lentoaseman ICAO-koodi: ").upper()

kordinaatit = hae_kordinaatit(rep1)
kordinaatit2 = hae_kordinaatit(rep2)

print(f"Etäisyys lentokenttien välillä on {distance.distance(kordinaatit, kordinaatit2).km:.2f} kilometriä.")
