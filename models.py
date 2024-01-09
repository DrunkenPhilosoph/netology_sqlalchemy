from main import Base
import sqlalchemy as sq
from sqlalchemy.orm import relationship


class Publicist(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.String(sq.String(length=255))

class Book(Base):

    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.String(sq.String(length=255))
    title = relationship("Publicist")

def create_tables(engine):
    Base.me