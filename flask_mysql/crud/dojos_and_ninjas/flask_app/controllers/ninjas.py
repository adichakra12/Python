from crypt import methods
from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import ninja, dojo


@app.route("/ninjas")
def show_dojos():
    return render_template('ninja.html', dojos= dojo.Dojo.get_all_dojos())

@app.route("/createNinja", methods = ["POST"])
def add_ninja_to_dojo():
    ninja.Ninja.add_ninja(request.form)
    return redirect("/")
