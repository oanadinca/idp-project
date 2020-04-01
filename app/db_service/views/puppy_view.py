import json

from sqlalchemy import literal_column
from sqlalchemy_imageattach.context import store_context

from app import db
from flask import abort, Blueprint

from app.db_service.models import Puppy, Match

api = Blueprint('puppy_view', __name__)


# def set_picture(request, puppy_id):
#     try:
#         puppy = db.session.query(Puppy).get(int(puppy_id))
#         with db.store_context(store):
#             puppy.picture.from_file(request.files['picture'])
#     except Exception:
#         db.session.rollback()
#         raise
#     db.session.commit()


def addPuppy(id: int, name: int, description: str, tag: str, photos: str):
    newPuppy = Puppy(id=id, name=name, description=description, tag=tag, photos=photos)

    db.session.add(newPuppy)
    db.session.commit()


@api.route('/api/puppies', method=['GET'])
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

@api.route('api/puppies/<int:id>', method=['GET'])
def getPuppy(id):
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

