from flask import Flask, jsonify, g
import mysql.connector

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='flight_game',
            user='matveib',
            password='salasana',
            autocommit=True,
            collation='utf8mb4_general_ci'
        )
    return g.db

def query_airport(icao_code):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT ident, name, municipality FROM airport WHERE ident = %s", (icao_code,))
    row = cursor.fetchone()
    cursor.close()
    return row

@app.route('/kenttä/<string:icao_code>', methods=['GET'])
def get_airport(icao_code):
    airport = query_airport(icao_code)
    if airport:
        result = {
            "ICAO": airport[0],
            "Name": airport[1],
            "Municipality": airport[2]
        }
        return jsonify(result)
    else:
        return jsonify({"error": "Airport not found"}), 404

@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True, port=3000)
