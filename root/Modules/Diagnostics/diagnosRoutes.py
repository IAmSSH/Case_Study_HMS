from root.Modules.Models.userstore import Patient
from flask import Flask, redirect, url_for, render_template, request, session, Blueprint
from flask import flash
from root import db
from sqlalchemy.exc import IntegrityError

diagnosRoutes = Blueprint("diagnosRoutes", __name__, static_folder="static",
                          template_folder="templates")


@diagnosRoutes.route('/diagnos', methods=['GET', 'POST'])
def diagnos():
    return "<h2>Ankit</h2>"
    """if request.method=="POST":
        ssn_id = request.form['patientid']
        patient_details = Patient.query.filter_by(ssn_id=ssn_id)"""
