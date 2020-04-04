from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.database import views, models
from app.database.models import Puppy, Owner, Match
from app.database import init_db

if Puppy.query.count() == 0:
	init_db.init_db_data()