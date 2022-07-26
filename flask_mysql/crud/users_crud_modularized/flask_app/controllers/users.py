from flask import render_template, request, redirect

from flask_app import app
from flask_app.model.users import User

@app.route('/')
def index():
    return redirect('/allUsers')

@app.route('/allUsers')
def all_users():
    return render_template("all_users.html", users=User.get_all())

@app.route('/user/addUser')
def add_one():
    return render_template("add_one.html")

@app.route('/user/create',methods=['POST'])
def create_one():
    User.create_one(request.form)
    return redirect('/allUsers')

@app.route('/user/editUser/<int:id>')
def edit_one(id):
    data ={"id":id}
    return render_template("edit_one.html",user=User.get_one(data))

@app.route('/user/showUser/<int:id>')
def show_one(id):
    data ={ 
        "id":id
    }
    return render_template("show_one.html", user=User.get_one(data))

@app.route('/user/updateUser',methods=['POST'])
def update_one():
    User.update_one(request.form)
    return redirect('/allUsers')

@app.route('/user/deleteUser/<int:id>')
def delete_one(id):
    user ={'id': id}
    User.delete_one(user)
    return redirect('/allUsers')