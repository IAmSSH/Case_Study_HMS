from flask import Flask , render_template , Blueprint ,session
from Modules.Models.userstore import userstore , db
admin = Blueprint("admin",__name__,static_folder="static",template_folder="templates")

#Admin page
@admin.route("/view")
def view():
    # db.session.query(userstore).delete()
    # db.session.commit()
    return render_template("Admin.html", values = userstore.query.all())