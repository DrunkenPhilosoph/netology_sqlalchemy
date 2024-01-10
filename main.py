import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publicist, Book

DSN = 'postgresql://postgres:1234@localhos:5433'
engine = sq.create_engine(DSN)

Session = sessionmaker(bing=engine)
session = Session()

create_tables(engine)

session.close()