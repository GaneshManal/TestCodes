from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Book(Base):
    """
    Sample Book 
    """
    __tablename__ = "book"
 
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    price = Column(Integer)
    available = Column(Boolean, default=True)

    def __init__(self, name, price=-1, available=True):
        """"""
        self.name = name
        self.price = price
        self.available = available
        self.quantity = 3
        self.issueed_quantity = 3

    def get_books(self):
        self.books.filter()

    def get_price(self):
        self.price

    def check_availability(self):
        return self.available


if __name__ == "__main__":
    # create engine and tables
    engine = create_engine('sqlite:///library.db', echo=True)
    Base.metadata.create_all(engine)

    b1 = Book()
    # write to database
    book = 'abc'
