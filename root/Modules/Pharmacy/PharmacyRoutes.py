from flask import Flask, redirect, url_for, render_template
from flask import request, session, Blueprint, flash
from sqlalchemy.exc import IntegrityError

from root.Modules.Models.userstore import Patient
from root import db

pharmacyRoutes = Blueprint("pharmacyRoutes", __name__, static_folder="static",
                          template_folder="templates")


@pharmacyRoutes.route('/pharmacy')
def test():
    return render_template('pharmacy.html')

@pharmacyRoutes.route('/pharmacy/get_details')
def get_details():
	id = int(request.args.get('patientid'))
	# print()
	return render_template('pharmacy.html', data=Patient.query.get(id))