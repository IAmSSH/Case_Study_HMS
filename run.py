# from flask import Flask, redirect, url_for, render_template, request, flash
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# # app.register_blueprint(admin, url_prefix="")
# app.secret_key = 'hello'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)


# class Patient(db.Model):
#     ssn_id = db.Column(db.Integer)
#     patient_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80))
#     age = db.Column(db.Integer)
#     admission_date = db.Column(db.Integer)
#     bed_type = db.Column(db.String(15))
#     address = db.Column(db.String(200))
#     city = db.Column(db.String(50))
#     state = db.Column(db.String(50))
#     status = db.Column(db.String(15))

# # Show Login route
# @app.route('/')
# def home():
#     print(Patient.query.all())
#     return render_template('base.html')



# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)




# from flask import Flask, redirect, url_for, render_template , request , session , flash
# from datetime import timedelta
# from flask_sqlalchemy import SQLAlchemy
# from Modules.Login.login import login
# from Modules.Admin.admin import admin
# from Modules.Patient.PatientRoutes import patientRoutes

# app = Flask(__name__)

# app.secret_key = "hello"

# app.register_blueprint(login,url_prefix="/")
# app.register_blueprint(admin,url_prefix="/")
# app.register_blueprint(patientRoutes,url_prefix="/")

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
from root import app

if __name__ == "__main__":
    app.run(debug=True)
