import redis
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/simmy', methods=['POST'])
def simmy():
    data = request.json
    return jsonify(data)
