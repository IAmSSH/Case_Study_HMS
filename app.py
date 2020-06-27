from flask import Flask, redirect, url_for, render_template , request , session , flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from Modules.Login.login import login
from Modules.Admin.admin import admin
# db.create_all()
app = Flask(__name__)
app.secret_key = "hello"
app.register_blueprint(login,url_prefix="/")
app.register_blueprint(admin,url_prefix="/")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class userstore(db.Model):
    time_stamp = db.Column("time_stamp", db.DateTime, primary_key=True)
    login = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, login, password, time_stamp):
        self.login = login
        self.password = password
        self.time_stamp = time_stamp


@app.route("/")
def home():
    return render_template("Base.html")
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
