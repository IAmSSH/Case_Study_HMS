from flask import Flask , render_template , Blueprint ,session
from root.Modules.Models.userstore import Medicine_Master, Patient, Track_Medicines ,userstore
from root import db

admin = Blueprint("admin",__name__,static_folder="static",template_folder="templates")

#Admin page
@admin.route("/view")
def view():
    # db.session.query(userstore).delete()
    # db.session.commit()
    track = Track_Medicines.query.all()
    print(track)
    for item in track:
        print(item)
    return render_template("Admin.html", track = track)