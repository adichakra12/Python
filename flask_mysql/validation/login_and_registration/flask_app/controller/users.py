from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.model.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
     return render_template('login_registration.html')

@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect('/logout')
    user = {
        'id': session['user_id']
    }
    return render_template("user.html", user = User.get_user_by_id(user))

@app.route('/login',methods=['POST'])
def login():
    user = User.get_user_by_email(request.form)

    if not user:
        flash("Invalid Email!","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password!","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/home')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/register',methods=['POST'])
def register():

    if not User.validate_user(request.form):
        return redirect('/')
    user ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.create_user(user)
    session['user_id'] = id

    return redirect('/home')