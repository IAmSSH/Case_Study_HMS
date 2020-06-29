from Modules.Models.userstore import userstore, db
from flask import Flask, redirect, url_for, render_template, request, session, Blueprint
from flask import flash
from datetime import datetime
from passlib.hash import sha256_crypt

login = Blueprint("login", __name__, static_folder="static",
                  template_folder="templates")

@login.route("/login", methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        found_user = None
        login = request.form["user_id"]
        password = request.form["password"]
        dateTimeObj = datetime.now()
        encrypted_password = userstore.query.filter_by(
            login=login).first().password 
        password_verification = sha256_crypt.verify(password,encrypted_password)
        if password_verification:
            session["login"] = login
            session["password"] = encrypted_password
            found_user = userstore.query.filter_by(
                login=login, password=encrypted_password).first()
        if found_user:
            return "Success!"
        else:
            flash("Invalid Credentials")
            return render_template("login.html")
    return render_template("login.html")

@login.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        login = request.form["user_id"]
        password = sha256_crypt.encrypt(request.form["password"])
        dateTimeObj = datetime.now()
        session["login"] = login
        session["password"] = password
        usr = userstore(login, password, dateTimeObj)
        db.session.add(usr)
        db.session.commit()
        # flash(f"Registering new User at {dateTimeObj} by user Id as {login}")
        return "Success!"
    else :
        return render_template("register.html")

@login.route("/logout")
def logout():
    flash("You have been successfully logged out!")
    session.pop("login",None)
    session.pop("password",None)
    return redirect(url_for('login'))

@login.route("/view")
def view():
	return render_template("Admin.html",values=userstore.query.all())