from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://mongo:27017/")
db = client["mydb"]
collection = db["users"]

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    collection.insert_one(data)
    return jsonify({"msg": "Data Added"})

@app.route('/get', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id':0}))
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
