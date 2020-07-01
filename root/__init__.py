from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "hello"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from root.Modules.Login.login import login
from root.Modules.Admin.admin import admin
from root.Modules.Patient.PatientRoutes import patientRoutes
from root.Modules.Pharmacy.PharmacyRoutes import pharmacyRoutes

app.register_blueprint(login, surl_prefix="/")
app.register_blueprint(admin, url_prefix="/")
app.register_blueprint(patientRoutes, url_prefix="/")
app.register_blueprint(pharmacyRoutes, url_prefix="/")