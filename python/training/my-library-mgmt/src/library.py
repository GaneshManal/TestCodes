from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Library(Base):
    """
    Sample Library 
    """
    __tablename__ = "library"
 
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def __init__(self, name):
        """"""
        self.name = name
        self.books = list()

    def get_books():
        pass



# create engine and tables
engine = create_engine('sqlite:///library.db', echo=True)
Base.metadata.create_all(engine)