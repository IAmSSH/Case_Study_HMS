from root.Modules.Models.userstore import Patient
from flask import Flask, redirect, url_for, render_template, request, session, Blueprint
from flask import flash
from root import db
from sqlalchemy.exc import IntegrityError

patientRoutes = Blueprint("patientRoutes", __name__, static_folder="static",
                  template_folder="templates")

@patientRoutes.route('/register_patient')
def register_patient():
    return render_template('patientRegistration.html')

@patientRoutes.route('/register_success')
def register_success():
    flash("Patient created successfully.", 'success')
    return redirect(url_for('patientRoutes.register_patient'))

@patientRoutes.route('/patients', methods=['GET', 'POST'])
def create_patient():
    if request.method == 'POST':
        # Check for duplicate in DB
        ssn_id = request.form['ssnid']
        try:
            name = request.form['name']
            age = request.form['age']
            admission_date = request.form['date']  # check
            bed_type = request.form['bed_type']
            address = request.form['address']
            city = request.form['city']
            state = request.form['state']
            status = 'Active'

            patient = Patient(
                ssn_id=ssn_id,
                name=name,
                age=age,
                admission_date=admission_date,
                bed_type=bed_type,
                address=address,
                city=city,
                state=state,
                status=status
            )

            db.session.add(patient)
            db.session.commit()

            return redirect(url_for('patientRoutes.register_success'))
        except IntegrityError:
            flash('A patient with given SSN ID already exists.', 'danger')
            return redirect(url_for('patientRoutes.register_patient'))

    else:
        return render_template('all_patients.html', user_list=Patient.query.all())

@patientRoutes.route('/test')
def test():
    return render_template('test.html')

@patientRoutes.route('/update_success')
def update_success():
    flash("Record updated successfully")
    return redirect(url_for('patientRoutes.update'))

@patientRoutes.route("/update", methods=['GET', 'POST'])
def update():
    if request.method == "POST":        
        if 'Get' in request.form:
            req_id = int(request.form['patientid'])
            found_patient = Patient.query.get(req_id)
            return render_template('updatePatient.html', patient_data=found_patient)

        elif 'Update' in request.form:
            patient_id = request.form['patientid']
            name = request.form['name']
            age = request.form['age']
            admission_date = request.form['date']  # check
            bed_type = request.form['bed_type']
            address = request.form['address']
            city = request.form['city']
            state = request.form['state']

            update_Record = Patient.query.filter_by(patient_id=patient_id).first()
            
            update_Record.name = name
            update_Record.age = age
            update_Record.admission_date = admission_date
            update_Record.bed_type = bed_type
            update_Record.address = address
            update_Record.city = city
            update_Record.state = state
            

            db.session.commit()
            
            return redirect(url_for('patientRoutes.update_success'))

    return render_template('updatePatient.html', patient_data=Patient())

@patientRoutes.route("/delete", methods=['GET', 'POST'])
def delete():
    if request.method == "POST":
        if 'Get' in request.form:
            req_id = int(request.form['patientid'])
            found_patient = Patient.query.get(req_id)

            if found_patient:
                return render_template('deletePatient.html', patient_data=found_patient)
            else:
                flash("No patient found matching the given ID")
                return redirect(url_for('patientRoutes.delete'))

        elif 'Delete' in request.form:
            patient_id = request.form['patientid']
            found_patient = Patient.query.get(patient_id)
            db.session.delete(found_patient)
            db.session.commit()
            return redirect(url_for('patientRoutes.create_patient'))

    return render_template('deletePatient.html', patient_data=Patient())

@patientRoutes.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        ssn_id = request.form['ssnid']
        patient = Test(ssn_id=ssn_id)

        db.session.add(patient)
        db.session.commit()

        return render_template('all_patients.html', user_list=Test.query.all())
    else:
        return render_template('all_patients.html', user_list=Test.query.all())

@patientRoutes.route('/clear_patients')
def clear():
    Patient.query.delete()
    db.session.commit()    
    flash('Patients cleared')
    return redirect(url_for('patientRoutes.create_patient'))