from flask import Flask
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
import json

db = PostgresqlDatabase('python_flask_project', user='python_flask_project',
                        password='12345', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Wine(BaseModel):
    name = CharField()
    price = DecimalField()
    country_state = CharField()
    region = CharField()
    product_type = CharField()
    varietal_type = CharField()
    description = TextField()
    image = CharField()
    flag = CharField()


db.connect()
db.drop_tables([Wine])
db.create_tables([Wine])

app = Flask(__name__)

file = open('master.json')
data = json.load(file)


@app.route('/')
def index():
    return 'This is working!'


@app.route('/get-json')
def get_json():
    return data


app.run(port=5000, debug=True)
