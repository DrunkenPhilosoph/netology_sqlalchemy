import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
import models
from models import Publicist, Book, Shop, Stock, Sale
from datetime import datetime
import json

DSN = 'postgresql://postgres:1234@localhost:5432'
engine = sq.create_engine(DSN)
Session = sessionmaker(engine)
session = Session()
models.create_tables(engine)

def add_data(path):
    with open(path, encoding='utf-8') as file:
        json_data = json.load(file)
        for item in json_data:
            print(item['model'])
            if item['model'] == 'publisher':
                publicists = Publicist(id=item['pk'], name=item['fields']['name'])
                session.add(publicists)
            if item['model'] == 'book':
                books = Book(id=item['pk'], title=item['fields']['title'], id_publisher=item['fields']['id_publisher'])
                session.add(books)
            if item['model'] == 'shop':
                shops = Shop(id=item['pk'], name=item['fields']['name'])
                session.add(shops)
            if item['model'] == 'stock':
                stocks = Stock(id=item['pk'], id_shop=item['fields']['id_shop'], id_book=item['fields']['id_book'], count=item['fields']['count'])
                session.add(stocks)
            if item['model'] == 'sale':
                sales = Sale(id=item['pk'], price=item['fields']['price'], date_sale=item['fields']['date_sale'], count=item['fields']['count'], id_stock=item['fields']['id_stock'])
                session.add(sales)
            session.commit()
    session.close()

def get_data(search):
    if search.isdigit():
        base_query = session.query(Book.title, Shop.name, Stock.count, Sale.price, Sale.date_sale).join(Book).join(Publicist).join(Sale).join(Shop).filter(Publicist.id == search)
    else:
        base_query = session.query(Book.title, Shop.name, Stock.count, Sale.price ,Sale.date_sale).join(Book).join(Publicist).join(Sale).join(Shop).filter(Publicist.name == search).all()

    result = ''
    for i in base_query:
        result += f"{i[0]} | {i[1]} | {i[3]} | {i[4].strftime('%d-%m-%Y')}\n"
    return result

if __name__ == '__main__':
    # add_data("tests_data.json")
    print(get_data(input('Введите id автора или название автора: ')))

