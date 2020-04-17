from app import db 

class TestModel(db.Model): 
    __tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String) 
    data = db.Column(db.String)

    def __init__(self, name, data): 
        self.name = name 
        self.data = data 

    def json(self): 
        return {'name': self.name, 'data': self.data}

    def save_to_db(self): 
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self): 
        db.session.delete(self)
        db.session.commit()

        