from crypt import methods
from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def show_all_dojos():
    dojos = Dojo.get_all_dojos()
    return render_template("ninjas_in_dojo.html", dojos = dojos)

@app.route("/newDojo", methods = ["POST"])
def create_one_dojo():
    Dojo.add_dojo_to_list(request.form)
    return redirect('/dojos')

@app.route("/dojo/<int:id>")
def ninjas_in_dojo(id):
    dojo = {
        'id':id
    }
    return render_template("dojo.html", dojos = Dojo.get_ninjas_in_dojo(dojo))
