from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Hello API"


@app.route("/add", methods=["GET"])
def add():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
    except (TypeError, ValueError):
        return jsonify({
            "error": "Bitte zwei gültige Zahlen als Query-Parameter 'a' und 'b' übergeben. Beispiel: /add?a=2&b=3"
        }), 400

    result = a + b

    return jsonify({
        "a": a,
        "b": b,
        "sum": result
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
