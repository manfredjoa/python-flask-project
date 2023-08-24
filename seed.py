from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
from app import Wine
from app import db
import json


# db = PostgresqlDatabase('wines', user='python_flask_project',
#                         password='12345', host='localhost', port=5432)


# class BaseModel(Model):
#     class Meta:
#         database = db


# class Wine(BaseModel):
#     name = CharField()
#     price = DecimalField()
#     country_state = CharField()
#     region = CharField()
#     product_type = CharField()
#     varietal_type = CharField()
#     description = TextField()
#     image = CharField()
#     flag = CharField()
#     correct = IntegerField(default=0)
#     incorrect = IntegerField(default=0)


db.connect()
db.drop_tables([Wine])
db.create_tables([Wine])

file = open('master.json')
data = json.load(file)

Wine.insert_many(data).execute()
