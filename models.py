import sqlalchemy as sq
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Publicist(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=255), nullable=False)
    book = relationship("Book", backref="publicist")

    def __str__(self):
        return f"{self.id} | {self.name}"
#
class Book(Base):
    __tablename__ = 'books'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=255), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)
    stock = relationship("Stock", backref="book")

    def __str__(self):
        return f"{self.id} | {self.title} | {self.id_publisher}"



class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("books.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    sale = relationship("Sale", backref="stock")

    def __str__(self):
        return f"{self.id} | {self.id_book} | {self.id_shop} | {self.count}"
#
class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=255), nullable=False)
    stock = relationship("Stock", backref="shop")

    def __str__(self):
        return f"{self.id} | {self.name}"
#
class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float)
    date_sale = sq.Column(sq.Date)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    def __str__(self):
        return f"{self.id} | {self.price} | {self.date_sale} | {self.id_stock}"
#
#
#
def create_tables(engine):
    Base.metadata.create_all(engine)