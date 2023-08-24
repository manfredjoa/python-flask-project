from peewee import *
from app import Wine
from app import db
import json

db.connect()
db.drop_tables([Wine])
db.create_tables([Wine])

file = open('master.json')
data = json.load(file)

Wine.insert_many(data).execute()
