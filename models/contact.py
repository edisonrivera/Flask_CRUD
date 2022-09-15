from utils.db import db


class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(15))
    last_name = db.Column(db.String(15))
    email = db.Column(db.String(30))
    phone = db.Column(db.String(10))

    def __init__(self, name, last_name, email, phone):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.phone = phone