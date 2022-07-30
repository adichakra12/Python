from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * from dojos;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in result:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def add_dojo_to_list(cls, data):
        query = "INSERT into dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return result
    
    @classmethod
    def get_ninjas_in_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print(result)
        dojo = cls(result[0])
        for item in result:
            ninja = {
                'id': item['ninjas.id'],
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'age': item['age'],
                'created_at': item['created_at'],
                'updated_at': item['updated_at']
            }
            dojo.ninjas.append(Ninja(ninja))
            return dojo

