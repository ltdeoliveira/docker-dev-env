from flask import Flask
from flask_restful import Resource, Api
import mysql.connector
import os

app = Flask(__name__)
api = Api(app)

class Cats(Resource):

    def __init__(self):
        pf = open("/run/secrets/db-password", 'r')

        host = os.environ.get('MYSQL_HOST')
        user = os.environ.get('MYSQL_USER')
        password = pf.read()
        database = os.environ.get('MYSQL_DATABASE')

        pf.close()

        connection = mysql.connector.connect(
            user=user, 
            host=host,
            password=password,
            database=database,
            auth_plugin='mysql_native_password'
        )

        cursor = connection.cursor()
        cursor.execute('SELECT * FROM cats')
        rec = []
        for c in cursor:
            rec.append(c)
        self.rec = rec

    def get(self):
        return self.rec

api.add_resource(Cats, '/')

if __name__ == '__main__':
    app.run(debug=True)