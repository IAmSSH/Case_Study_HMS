from flask import Flask,redirect, url_for, render_template , request , session , flash , Blueprint
from Modules.Models.userstore import userstore
login = Blueprint("login",__name__,static_folder="static",template_folder="templates")

@login.route("/login" , methods=["GET","POST"])
def auth():
    if request.method == "POST":
        login = request.form["user_id"]
        password = request.form["password"]
        session["login"] = login
        session["password"] = password
        found_user = userstore.query.filter_by(login = login , password = password).first()
        if found_user :
            return "Success!"
        else:
            flash("Invalid Credentials")
            return render_template("login.html")

    return render_template("login.html")