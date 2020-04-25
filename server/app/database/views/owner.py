import json
from flask import request, jsonify

from sqlalchemy import literal_column
from sqlalchemy_imageattach.context import store_context

from app import db
from flask import abort, Blueprint

from app.database.models import Owner, Match

api = Blueprint('owner', __name__)

@api.route('/api/owners', methods=['GET'])
def get_owners():
    try:
        query_result = db.session.query(Owner).all()
    except:
        # When the query results in an exception return a server error.
        return abort(500)

    owners = []

    for owner in query_result:
        owners.append({
            'id': owner.id,
            'owner': owner.name,
            'description': owner.description,
        })

    json_list = json.dumps(owners, ensure_ascii=False)

    return json_list


@api.route('/api/owner', methods=['GET'])
def get_owner():

    id = int(request.args.get('id'))
    try:
        query_result = db.session.query(Owner).filter(Owner.id == id).all()
    except:
        # When the query results in an exception return a server error.
        return abort(500)
        
    return query_result[0].to_json()


@api.route('/api/owner', methods=['POST', 'PUT'])
def post_or_update_owner():

    my_json = {}
    my_json['id'] = int(request.args.get('id'))
    my_json['name'] = (request.args.get('name'))
    my_json['description'] = (request.args.get('description'))

    owner = Owner(my_json)

    try:
        if request.method == 'POST':
            owner.save()
        else:
            id = int(request.args.get('id'))
            query_result = db.session.query(Owner).filter(Owner.id == id).all()
            query_result[0].delete()
            owner.save()
    except Exception as e:
        print(e)
        return abort(406)

    response = "Successfully saved owner"

    return jsonify(response), 200

@api.route('/api/owner', methods=['DELETE'])
def delete_owner():

    id = int(request.args.get('id'))

    try:
        query_result = db.session.query(Owner).filter(Owner.id == id).all()
        query_result[0].delete()
    except Exception as e:
        print(e)
        return abort(406)
        
    response = "Successfully deleted owner"

    return jsonify(response), 200