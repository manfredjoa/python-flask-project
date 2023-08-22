from flask import Flask
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
import json


db = PostgresqlDatabase('wines', user='python_flask_project',
                        password='12345', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db

# Used sed -i '' -e 's/JSONFieldName/python_field_name/g' master.json to change json field names through terminal


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

file = open('master.json')
data = json.load(file)

Wine.insert_many(data).execute()

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is working!'


app.run(port=5000, debug=True)
