from flask_app.config.mysqlconnection import connectToMySQL
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO user (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        result = connectToMySQL("login_registration_schema").query_db(query,data)
        return result

    @classmethod
    def get_user_by_email(cls,data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        result = connectToMySQL("login_registration_schema").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        result = connectToMySQL("login_registration_schema").query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user;"
        result = connectToMySQL("login_registration_schema").query_db(query)
        users = []
        for user in result:
            users.append( cls(user) )
        return users


    @staticmethod
    def validate_user( user ):
        is_valid = True
        query = "SELECT * FROM user WHERE email = %(email)s;"
        result = connectToMySQL("login_registration_schema").query_db(query,user)
        if len(result) >= 1:
            flash("The email you provided has a linked account. Try again with a different email or log in to an existing account.","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Please provide a valid email address!", "register")
            is_valid = False
        if len(user['email'])  < 1:
            flash("Email cannot be left blank!", "register")
            is_valid = False
        if len(user['first_name']) < 1:
            flash("First name cannot be left blank!","register")
            is_valid= False
        if len(user['last_name']) < 1:
            flash("Last name cannot be left blank!","register")
            is_valid= False
        if len(user['password']) < 6:
            flash("Password must be at least 6 characters!","register")
            is_valid= False
        if user['password'] != user['confirm']:
            flash("Passwords don't match! Please try again.","register")
        return is_valid

