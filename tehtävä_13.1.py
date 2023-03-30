# Tehtävä 13.1

from flask import Flask, jsonify
import json

# http://127.0.0.1:3000/alkuluku/31/

app = Flask(__name__)

@app.route('/alkuluku/<int:luku>/')
def alkuluku(luku):
    try:

        alkuluku = True

        for i in range(2, int(luku)):
            if luku % i == 0:
                alkuluku = False
                break

        vastaus = {
            "Number": luku, "isPrime": alkuluku
        }

        jsonvastaus = json.dumps(vastaus)
        return jsonify(vastaus)

    except:
        return "Error: Invalid input"

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
