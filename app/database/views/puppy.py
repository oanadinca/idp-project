import json
from flask import request

from sqlalchemy import literal_column
from sqlalchemy_imageattach.context import store_context

from app import db
from flask import abort, Blueprint

from app.database.models import Puppy, Match

api = Blueprint('puppy', __name__)


@api.route('/api/puppies', methods=['GET'])
def getAllPuppies():
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

@api.route('/api/puppies/<int:id>', methods=['GET'])
def getPuppy(id):
    try:
        query_result = db.session.query(Puppy).filter(Puppy.id == id).all()
    except:
        # When the query results in an exception return a server error.
        return abort(500)
        
    return query_result[0].to_json()

