from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class User(Base):
    """
    Sample Book 
    """
    __tablename__ = "user"
 
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    age = Column(Integer)

    def __init__(self, name, age=-1):
        """"""
        self.name = name
        self.age = age


# create engine and tables
engine = create_engine('sqlite:///library.db', echo=True)
Base.metadata.create_all(engine)
