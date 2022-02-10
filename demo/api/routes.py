from crypt import methods
from flask import Blueprint, json, request



api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getall', methods=['GET'])
def getAll():
    with api.open_resource('sample.json', 'r') as db:
        data = json.load(db)
    return data, 200

@api.route('/getone/<id>', methods=['GET'])
def getOne(id):
    id = int(id)
    with api.open_resource('sample.json', 'r') as db:
        data = json.load(db)
    try:
        student = data['students'][id-1]
        return student, 200
    except:
        return {'message':'Sorry, that student does not exist yet!'}, 404


@api.route('/changename/<id>', methods=['POST'])
def changeName(id):
    id = int(id)
    try:
        name = request.json['name']
        with api.open_resource('sample.json', 'r') as db:
            data = json.load(db)
        student = data['students'][id-1]
        student['name'] = name
        
        return student, 200
    except:
        return {'message':'Sorry, that student does not exist yet!'}, 501
