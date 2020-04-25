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
        return '<Puppy id={} name={} description={} tag={}>'.format(self.id, self.name, self.description, self.tag)

    def __init__(self, json_client):
        self.id = json_client['id']
        self.name = json_client['name']
        self.description = json_client['description']
        self.tag = json_client['tag']

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, json_client):
        self.name = json_client['name']
        self.description = json_client['description']
        self.tag = json_client['tag']
        self.match = json_client['match']
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_json(self):
        json = {
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'tag' : self.tag
        }
        return json


class Owner(db.Model):
    __tablename__ = 'owner'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True)
    description = db.Column(db.Text)
    match = db.relationship("Match", uselist=False, back_populates="owner")

    def __repr__(self):
        return '<Owner id={} name={}>'.format(self.id, self.name)

    def __init__(self, json_client):
        self.id = json_client['id']
        self.name = json_client['name']
        self.description = json_client['description']

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, json_client):
        self.name = json_client['name']
        self.description = json_client['description']
        self.match = json_client['match']
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_json(self):
        json = {
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
        }
        return json


class Match(db.Model):
    __tablename__ = 'match'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppy.id'))
    owner = db.relationship("Owner", back_populates="match")
    puppy = db.relationship("Puppy", back_populates="match")


    def __repr__(self):
        return '<Match id={} owner_id={} puppy_id={}>'.format(self.id, self.owner_id, self.puppy_id)

    def __init__(self, json_client):
        self.id = json_client['id']
        self.owner_id = json_client['owner_id']
        self.puppy_id = json_client['puppy_id']

    def save(self):
        puppy = Puppy.query.filter_by(id=self.puppy_id).one()
        owner = Owner.query.filter_by(id=self.owner_id).one()
        self.owner = owner
        self.puppy = puppy
        db.session.add(self)
        db.session.commit()

    def update(self, json_client):
        self.owner_id = json_client['owner_id']
        self.puppy_id = json_client['puppy_id']
        puppy = Puppy.query.filter_by(id=self.puppy_id).one()
        owner = Owner.query.filter_by(id=self.owner_id).one()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_json(self):
        json = {
            'id' : self.id,
            'owner_id' : self.owner_id,
            'puppy_id' : self.puppy_id,
        }
        return json