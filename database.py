from app import app, db
from app.db_service.models import Puppy , Owner, Match

# This file makes it possible to access the database from shell.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Puppy': Puppy, 'Owner': Owner, 'Match': Match}