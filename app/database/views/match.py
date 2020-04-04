import json

from sqlalchemy import literal_column

from app import db
from flask import abort, Blueprint

from app.database.models import Owner, Puppy, Match

api = Blueprint('match', __name__)


@api.route('/api/matches')
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