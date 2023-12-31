from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('wines', user='python_flask_project',
                        password='12345', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Wine(BaseModel):
    name = CharField()
    country_state = CharField()
    region = CharField()
    product_type = CharField()
    varietal_type = CharField()
    description = TextField()
    image = CharField()
    flag = CharField()
    correct = IntegerField(default=0)
    incorrect = IntegerField(default=0)


app = Flask(__name__)


@app.route('/')
def index():
    return 'This is the root route.'


@app.route('/wines', methods=['GET', 'POST'])
@app.route('/wines/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Wine.get(Wine.id == id)))
        else:
            wine_list = []
            for wine in Wine.select():
                wine_list.append(model_to_dict(wine))
            return jsonify(wine_list)

    if request.method == 'PUT':
        body = request.get_json()
        Wine.update(body).where(Wine.id == id).execute()
        return "Wine " + str(id) + " has been updated."

    if request.method == 'POST':
        new_wine = dict_to_model(Wine, request.get_json())
        new_wine.save()
        return f"{new_wine.name} has been added."

    if request.method == 'DELETE':
        Wine.delete().where(Wine.id == id).execute()
        return "Wine " + str(id) + " has been deleted."


if __name__ == '__main__':
    app.run(port=5000, debug=True)
