import json

from sqlalchemy import literal_column

from app import db
from flask import abort, Blueprint

from app.db_service.models import Owner, Puppy, Match

api = Blueprint('match_view', __name__)


def addMatch(id: int, owner_id: int, puppy_id: int):
    newMatch = Match(id=id, owner_id=owner_id, puppy_id=puppy_id)

    db.session.add(newMatch)
    db.session.commit()


@api.route('/api/matches')
def getMatches():
    try:
        query_result = db.session.query(Match).all()
    except:
        # When the query results in an exception return a server error.
        return abort(500)

    matches = []

    for match in query_result:
        match.append({
            'id': match.id,
            'owner_id': match.owner_id,
            'puppy_id': match.puppy_id,
        })

    json_list = json.dumps(matches, ensure_ascii=False)

    return json_list