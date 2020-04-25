import json
from flask import request, jsonify

from sqlalchemy import literal_column
from sqlalchemy_imageattach.context import store_context

from app import db
from flask import abort, Blueprint
from flask_cors import CORS, cross_origin

from app.database.models import Puppy, Match

api = Blueprint('puppy', __name__)


@api.route('/api/puppies', methods=['GET'])
@cross_origin() # allow all origins all methods.
def get_puppies():
    try:
        query_result = db.session.query(Puppy).all()
    except:
        # When the query results in an exception return a server error.
        return abort(500)

    puppies = []

    for puppy in query_result:
        puppies.append({
            'id': puppy.id,
            'name': puppy.name,
            'description': puppy.description,
            'tag': puppy.tag
        })

    json_list = json.dumps(puppies, ensure_ascii=False)

    return json_list

@api.route('/api/puppy', methods=['GET'])
@cross_origin() # allow all origins all methods.
def get_puppy():

    id = int(request.args.get('id'))
    try:
        query_result = db.session.query(Puppy).filter(Puppy.id == id).all()
    except:
        # When the query results in an exception return a server error.
        return abort(500)
        
    return query_result[0].to_json()


@api.route('/api/puppy', methods=['POST','PUT'])
@cross_origin() # allow all origins all methods.
def post_or_update_puppy():

    my_json = {}
    my_json['id'] = int(request.args.get('id'))
    my_json['name'] = (request.args.get('name'))
    my_json['description'] = (request.args.get('description'))
    my_json['tag'] = (request.args.get('tag'))

    puppy = Puppy(my_json)

    try:
        if request.method == 'POST':
            puppy.save()
        else:
            id = int(request.args.get('id'))
            query_result = db.session.query(Puppy).filter(Puppy.id == id).all()
            query_result[0].delete()
            puppy.save()
    except Exception as e:
        print(e)
        return abort(406)

    response = "Successfully saved puppy"

    return jsonify(response), 200

@api.route('/api/puppy', methods=['DELETE'])
@cross_origin() # allow all origins all methods.
def delete_puppy():

    id = int(request.args.get('id'))

    try:
        query_result = db.session.query(Puppy).filter(Puppy.id == id).all()
        query_result[0].delete()
    except Exception as e:
        print(e)
        return abort(406)
        
    response = "Successfully deleted puppy"

    return jsonify(response), 200

    
    
