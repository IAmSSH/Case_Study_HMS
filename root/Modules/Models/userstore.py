from root import db

class userstore(db.Model):
    time_stamp = db.Column("time_stamp", db.DateTime, primary_key=True)
    login = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, login, password, time_stamp):
        self.login = login
        self.password = password
        self.time_stamp = time_stamp

class Patient(db.Model):
    ssn_id = db.Column(db.String(50), unique=True)
    patient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    admission_date = db.Column(db.Integer)
    bed_type = db.Column(db.String(15))
    address = db.Column(db.String(200))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    status = db.Column(db.String(15))