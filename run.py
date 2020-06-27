from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.register_blueprint(admin, url_prefix="")
app.secret_key = 'hello'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

class Test(db.Model):
    ssn_id = db.Column(db.Integer)
    patient_id = db.Column(db.Integer, primary_key=True)


db.create_all()        

@app.route('/')
def home():
    print(Patient.query.all())
    return render_template('Base.html')

@app.route('/register_patient')
def register_patient():
    return render_template('patientRegistration.html')

@app.route('/patients', methods=['GET', 'POST'])
def create_patient():
    if request.method == 'POST':
        ssn_id = request.form['ssnid']
        name = request.form['name']
        age = request.form['age']
        admission_date = request.form['date'] # check 
        bed_type = request.form['bed_type']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        status = 'Active'

        patient = Patient(
        ssn_id = ssn_id,
        name = name,
        age = age,
        admission_date = admission_date,
        bed_type = bed_type,
        address = address,
        city = city,
        state = state,
        status = status 
            )

        db.session.add(patient)
        db.session.commit()
        
        return render_template('all_patients.html', user_list=Patient.query.all())
    else:
        return render_template('all_patients.html', user_list=Patient.query.all())

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        ssn_id = request.form['ssnid']
        patient = Test(ssn_id = ssn_id)

        db.session.add(patient)
        db.session.commit()

        return render_template('all_patients.html', user_list=Test.query.all())
    else:
        return render_template('all_patients.html', user_list=Test.query.all())

if __name__ == '__main__':
    app.run(debug=True)