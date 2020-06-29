# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "hello"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from root.Modules.Login.login import login
from root.Modules.Admin.admin import admin
from root.Modules.Patient.PatientRoutes import patientRoutes

app.register_blueprint(login,url_prefix="/")
app.register_blueprint(admin,url_prefix="/")
app.register_blueprint(patientRoutes,url_prefix="/")