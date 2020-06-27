from flask import Flask,render_template,Blueprint

login = Blueprint("login",__name__,static_folder="static",template_folder="templates")

@login.route("/login")
def auth():
    return "This is the Auth Page!"