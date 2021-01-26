from flask import Flask, request, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

cluster = MongoClient('mongodb+srv://aghazadeh:salam123@cluster0.yrec2.mongodb.net/<dbname>?retryWrites=true&w=majority')
mdb = cluster['test']
collection = mdb['test']



@app.route('/api/v1/send-data/', methods=['GET', 'POST'])
def send_data():
    if request.method == 'POST':
        req = {'message': 'success'}
        # req =  request.json or request.form
        collection.insert_one(req)
        print(req)
        return jsonify({"success": "success"})


if __name__ == '__main__':
    app.run(debug=True)