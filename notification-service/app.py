from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/notify')
def notify():
    return jsonify({"message": "notification sent"})

app.run(host="0.0.0.0", port=8004)