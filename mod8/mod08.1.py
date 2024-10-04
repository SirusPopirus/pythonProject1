import mysql.connector

conn = mysql.connector.connect(
    host= 'localhost',
    port= 3306,
    database= 'flight_game',
    user= 'matveib',
    password= 'Legotori21',
    autocommit=True,
    collation= 'utf8mb4_general_ci'
    )
rep = input("Syötä lentoaseman ICAO-koodi: ").upper()

def print_countries(rep):
    sql = "SELECT name, municipality FROM airport"
    sql += f"WHERE ident = '{rep}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Lentoaseman nimi on {row[0]} ja se on sijaintikunnassa {row[1]}")
            return

print_countries(rep)


#GRANT SELECT, INSERT, UPDATE ON flight_game.* TO matveib@localhost;