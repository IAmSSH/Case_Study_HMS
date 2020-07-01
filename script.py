from root import db

db.create_all()

from root.Modules.Models.userstore import Medicine_Master, Patient, Track_Medicines

patient_1 = Patient(ssn_id=12, name='asd', age=32, admission_date=12, bed_type='asd', address='asd', city='asd', state='asd', status='asd')
med_1 = Medicine_Master(med_name='sad', quantity=12, rate=21)

db.session.add(patient_1)
db.session.add(med_1)

db.session.commit()

pid = Patient.query.get(1).patient_id
mid = Medicine_Master.query.get(1).med_id

track_1 = Track_Medicines(patient_id=pid, med_id=mid, quantity_issued=213)

db.session.add(track_1)
db.session.commit()