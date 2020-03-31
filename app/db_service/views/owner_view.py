import json

from sqlalchemy import literal_column

from app import db
from flask import abort, Blueprint

from app.db_service.models import Owner

api = Blueprint('owner_view', __name__)


def addOwner(id: int, name: str, description: str):
    newOwner = Owner(id=id, name=name, description=description)

    db.session.add(newOwner)
    db.session.commit()


@api.route('/api/owners')
def getOwners():
    try:
        query_result = db.session.query(Owner).all()
    except:
        # When the query results in an exception return a server error.
        return abort(500)

    owners = []

    for owner in query_result:
        owner.append({
            'id': owner.id,
            'owner': owner.name,
            'description': owner.description,
        })

    json_list = json.dumps(owners, ensure_ascii=False)

    return json_list