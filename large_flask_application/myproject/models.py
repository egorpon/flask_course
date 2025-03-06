from myproject import db

class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)

    owner = db.relationship('Owner', backref = 'puppy', uselist = False)
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f'Puppy name is {self.name} and owner is {self.owner.name}' 
        return f'Puppy name is {self.name} and has no owner yet!'

class Owner(db.Model):
    __tablename__ = 'owner'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    id_pup = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, id_pup):
        self.name = name
        self.id_pup = id_pup

    def __repr__(self):
        return f'Owner name: {self.name}'