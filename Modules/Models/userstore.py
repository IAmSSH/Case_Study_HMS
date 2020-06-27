from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class userstore(db.Model):
    time_stamp = db.Column("time_stamp", db.DateTime, primary_key=True)
    login = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, login, password, time_stamp):
        self.login = login
        self.password = password
        self.time_stamp = time_stamp