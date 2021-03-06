from flask import Flask, redirect, url_for, render_template , request , session , flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from Modules.Login.login import login
app = Flask(__name__)
app.register_blueprint(login,url_prefix="/")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def home():
    return render_template("Base.html")
if __name__ == "__main__":
	app.run(debug=True)
