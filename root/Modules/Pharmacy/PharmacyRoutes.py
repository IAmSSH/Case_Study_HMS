from flask import Flask, redirect, url_for, render_template
from flask import request, session, Blueprint, flash
from sqlalchemy.exc import IntegrityError
from root.Modules.Models.userstore import Track_Medicines
from root.Modules.Models.userstore import Patient, Medicine_Master
from root import db

pharmacyRoutes = Blueprint("pharmacyRoutes", __name__, static_folder="static",
                           template_folder="templates")


@pharmacyRoutes.route('/medicines')
def view_all():
    return render_template('all_meds.html', med_list=Medicine_Master.query.all())


@pharmacyRoutes.route('/pharmacy')
def test():
    return render_template('pharmacy.html')

@pharmacyRoutes.route('/submit',methods=['GET','POST'])
def linkDetails():
    if request.method == 'POST':
        id = request.form["pid"]
        for item in meds_to_issue:
            track = Track_Medicines(med_id = item["meds"].med_id, patient_id = id ,quantity_issued = item["qty"])
            db.session.add(track)
            db.session.commit()
            print(track.id , track.med_id , track.patient_id , track.quantity_issued)
        return "Success"

meds_to_issue = []
@pharmacyRoutes.route('/pharmacy/get_details', methods=['GET', 'POST'])
def get_details():
    if request.method == 'GET':
        id = int(request.args.get('patientid'))
        # print()
        med_id = request.args.get('med_id')
        found_med = None
        avl = ""
        if med_id:
            found_med = Medicine_Master.query.get(med_id)
            if found_med:
            	avl = found_med.quantity
            	return render_template('pharmacy.html', data=Patient.query.get(id), id=id, avl=avl, found=found_med,meds_to_issue=meds_to_issue)
        return render_template('pharmacy.html', data=Patient.query.get(id), id=id, avl=avl, meds_to_issue=meds_to_issue)
    else:
        id = request.form["patientid"]
        qty = request.form["med_qty_req"]
        med_id = request.form["med_id"]
        found_med = Medicine_Master.query.get(med_id)
        amount = int(qty)*int(found_med.rate)
        dict_item = {"meds": None, "qty": None, "amount": None}
        dict_item["meds"] = found_med
        dict_item["qty"] = qty
        dict_item["amount"] = amount
        print(dict_item)
        meds_to_issue.append(dict_item)
        return render_template('pharmacy.html', data=Patient.query.get(id), id=id,
                               meds_to_issue=meds_to_issue)
