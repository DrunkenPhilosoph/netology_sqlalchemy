import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
import models
from models import create_tables, Publicist, Book
import json

DSN = 'postgresql://postgres:1234@localhos:5433?charset=utf-8'
engine = sq.create_engine(DSN)
Session = sessionmaker(engine)
session = Session()
models.create_tables(engine)

with open("tests_data.json", encoding='utf-8') as file:
    json_data = json.load(file)
    print(json_data)
# data = json.load("test_data.json", encoding="unicode", errors='ignore')
# print(data)


session.close()