from root import db


class userstore(db.Model):
    time_stamp = db.Column("time_stamp", db.DateTime, primary_key=True)
    login = db.Column(db.String(100))
    password = db.Column(db.String(100))


class Patient(db.Model):
    ssn_id = db.Column(db.String(50), unique=True)
    patient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    # Change to date type
    admission_date = db.Column(db.Integer)
    bed_type = db.Column(db.String(15))
    address = db.Column(db.String(200))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    status = db.Column(db.String(15))
    med_list = db.relationship('Track_Medicines', backref='patient', lazy=True)


class Medicine_Master(db.Model):
    med_id = db.Column(db.Integer, primary_key=True)
    med_name = db.Column(db.String(50), unique=True)
    quantity = db.Column(db.Integer)
    rate = db.Column(db.Integer)
    patient = db.relationship('Track_Medicines', backref='medicine', lazy=True)


class Track_Medicines(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'))
    med_id = db.Column(db.Integer, db.ForeignKey('medicine__master.med_id'))
    quantity_issued = db.Column(db.Integer)


# patient_1 = Patient(ssn_id=12, name='asd', age=32, admission_date=12, bed_type='asd', address='asd', city='asd', state='asd', status='asd')
# med_1 = Medicine_Master(med_name='sad', quantity=12, rate=21)

# track_1 = Track_Medicines(patient_id=patient_1.patient_id, med_id=med_1.med_id, quantity_issued=213)



# Patient.query.get(1).med_list[0].medicine.med_name