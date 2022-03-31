import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from book import *
from user import *

if __name__ == '__main__':
    engine = create_engine('sqlite:///library.db', echo=True)
    Base = declarative_base()

    # create tables
    Base.metadata.create_all(engine)

    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create book objects  
    book = Book("Head First Python", 100)
    session.add(book)

    # Create user object  
    user = User("Ganesh Manal", 30)
    session.add(user)

    # commit the record the database
    session.commit()
