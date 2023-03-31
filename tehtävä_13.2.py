from flask import Flask, Response, jsonify
import json
import mysql.connector

app = Flask(__name__)


# http://127.0.0.1:3000/airport/ + icao


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user="user2",
    password="pass2word_",
    autocommit=True
    )


@app.route('/airport/<icao>')
def search_airport(icao):
    try:
        sql = f"SELECT ident, name, municipality FROM airport WHERE ident ='{icao}'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        response = {"ICAO": result[0], "Name": result[1], "Municipality": result[2]}
        return jsonify(response)

    except ValueError:
        response = {"message": "invalid request"}
        response_json = json.dumps(response)
        return Response(response=response_json, status=400, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(status):
    response = {"status": "404", "message": "Not found"}
    response_json = json.dumps(response)
    return Response(response=response_json, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
