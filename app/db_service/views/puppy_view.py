import json

from sqlalchemy import literal_column

from app import db
from flask import abort, Blueprint

from app.db_service.models import Puppy

api = Blueprint('puppy_view', __name__)


def addPuppy(id: int, name: int, description: str, tag: str, photos: str):
    newPuppy = Puppy(id=id, name=name, description=description, tag=tag, photos=photos)

    db.session.add(newPuppy)
    db.session.commit()


@api.route('/api/puppies', method="GET")
def getAllPuppies():
    try:
        query_result = db.session.query(Puppy).all()
    except:
        # When the query results in an exception return a server error.
        return abort(500)

    puppies = []

    for puppy in query_result:
        puppy.append({
            'id': puppy.id,
            'owner': puppy.name,
            'description': puppy.description,
            'tag': puppy.tag,
            'photos': puppy.photos
        })

    json_list = json.dumps(puppies, ensure_ascii=False)

    return json_list

@api.route('api/pupies/<id>', method="GET")
def getPuppy(id: int):
    try:
        query_result = db.session.query(Puppy).filter(Puppy.id == id).all()
    except:
        # When the query results in an exception return a server error.
        return abort(500)


    puppy = query_result[0].append({
        'id': puppy.id,
        'owner': puppy.name,
        'description': puppy.description,
        'tag': puppy.tag,
        'photos': puppy.photos
    })
        
    json_list = json.dumps(, ensure_ascii=False)

    return json_list

