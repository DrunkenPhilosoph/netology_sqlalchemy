import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker, declarative_base

DSN = 'postgresql://postgres:1234@localhos:5433'
engine = sq.create_engine(DSN)

Session = sessionmaker(bing=engine)
session = Session()

Base = declarative_base()

class Person(Base):
    __tablename__ = 'ukr_mvd_person'

    id = sq.Column(sq.Integer)
    rus_name = sq.String(sq.String(lenght=100))
    ukr_name = sq.String(sq.String(lenght=100))


def create_tables(engine):
    Base.me
session.close()