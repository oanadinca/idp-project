from app import db

class Puppy(db.Model):
    __tablename__ = 'puppy'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True)
    description = db.Column(db.Text)
    tag = db.Column(db.String(100), nullable=False, index=True)
    photo = db.Column(db.String(100))
    match = db.relationship("Match", uselist=False, back_populates="puppy")

    def __repr__(self):
        return '<Puppy id={} name={} description={} tag={}, photos={}>'.format(self.id, self.name, self.description, self.tag, self.photos)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Owner(db.Model):
    __tablename__ = 'owner'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True)
    description = db.Column(db.Text)
    match = db.relationship("Match", uselist=False, back_populates="owner")

    def __repr__(self):
        return '<Owner id={} name={} description={}>'.format(self.id, self.name, self.description)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Match(db.Model):
    __tablename__ = 'match'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppy.id'))
    owner = db.relationship("Owner", back_populates="match")
    puppy = db.relationship("Puppy", back_populates="match")


    def __repr__(self):
        return '<Match id={} owner_id={} puppy_id={}>'.format(self.id, self.owner_id, self.puppy_id)

    def as_dict(self):
        return {column.id: getattr(self, column.id) for column in self.__table__.columns}