import json
from flask import request, jsonify

from sqlalchemy import literal_column
from sqlalchemy_imageattach.context import store_context

from app import db
from flask import abort, Blueprint

from app.database.models import Puppy, Match, Owner

api = Blueprint('match', __name__)


@api.route('/api/matches', methods=['GET'])
def getMatches():
    try:
        query_result = db.session.query(Match).all()
    except:
        # When the query results in an exception return a server error.
        return abort(500)

    matches = []

    for match in query_result:
        matches.append({
            'id': match.id,
            'owner_id': match.owner_id,
            'puppy_id': match.puppy_id,
        })

    json_list = json.dumps(matches, ensure_ascii=False)

    return json_list


@api.route('/api/match', methods=['GET'])
def get_match():

    id = int(request.args.get('id'))
    try:
        query_result = db.session.query(Match).filter(Match.id == id).all()
    except:
        # When the query results in an exception return a server error.
        return abort(500)
        
    return query_result[0].to_json()


@api.route('/api/match', methods=['POST', 'PUT'])
def post_or_update_match():

    my_json = {}
    my_json['id'] = int(request.args.get('id'))
    my_json['owner_id'] = (request.args.get('owner_id'))
    my_json['puppy_id'] = (request.args.get('puppy_id'))

    match = Match(my_json)

    try:
        if request.method == 'POST':
            match.save()
        else:
            id = int(request.args.get('id'))
            query_result = db.session.query(Match).filter(Match.id == id).all()
            query_result[0].delete()
            match.save()
    except Exception as e:
        print(e)
        return abort(406)

    response = "Successfully saved match"

    return jsonify(response), 200

@api.route('/api/match', methods=['DELETE'])
def deleteMatch():

    id = int(request.args.get('id'))

    try:
        query_result = db.session.query(Match).filter(Match.id == id).all()
        query_result[0].delete()
    except Exception as e:
        print(e)
        return abort(406)
        
    response = "Successfully deleted match"

    return jsonify(response), 200