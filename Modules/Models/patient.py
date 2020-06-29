from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Patient(db.Model):
    ssn_id = db.Column(db.Integer)
    patient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    admission_date = db.Column(db.Integer)
    bed_type = db.Column(db.String(15))
    address = db.Column(db.String(200))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    status = db.Column(db.String(15))