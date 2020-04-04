from app import app
from app.database.views import puppy, owner, match

app.register_blueprint(puppy.api)
app.register_blueprint(owner.api)
app.register_blueprint(match.api)