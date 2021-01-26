import uuid
from flask import Flask, request, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

cluster = MongoClient('mongodb+srv://aghazadeh:salam123@cluster0.yrec2.mongodb.net/<dbname>?retryWrites=true&w=majority')
mdb = cluster['test']
collection = mdb['test']
path = '/Users/husubayli/Desktop/Document/freelance/flask_mongodb_app/auto_increment.txt'


@app.route('/api/v1/send-data/', methods=['GET', 'POST'])
def send_data():
    if request.method == 'POST':
        # req = {'message': 'success'}
        # req =  request.json or request.form
        raw_id = uuid.uuid1()
        membership_id = str(raw_id.int)[:5]

        with open(path, 'r+') as file:
            id_list = file.read()
            print(id_list, 'malas')
            if id_list == '':
                user_id = 0
            else:
                user_id = int(id_list)
            user = {"id": user_id+1, "username": "Murad", 'membership_id': membership_id + str(user_id)}
            user_id_str = str(user['id'])
        with open(path, 'w') as f:
            f.write(user_id_str)
        collection.insert_one(user)
        print(user)
        return jsonify({'message': 'success'})




users = [

]

# from .models import *

if __name__ == '__main__':
    app.run(debug=True)