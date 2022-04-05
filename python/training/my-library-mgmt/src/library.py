from logging import exception
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


    def add_book():
        pass

    def update_book():
        pass

    def issue_book():
        pass

    def return_book():
        pass


# create engine and tables
engine = create_engine('sqlite:///library.db', echo=True)
Base.metadata.create_all(engine)

if __name__ == "__main__":
    choice = True
    while choice:
        try:
            print("1 - book, 2 - user, 3- library")
            entity = int(input("select entity - "))
            if entity not in [1, 2, 3]:
                raise exception

            if entity in [1, 2]:
                print("1 - Add, 2 - read, 3 - update, 4 - delete")
                operation = int(input("select operation - "))
                if operation not in [1, 2, 3, 4]:
                    raise exception
            else:
                print("1 - issue book, 2 - return book")
                operation = int(input("select operation - "))
                if operation not in [1, 2]:
                    raise exception
        except:
            print("invalid input !")
            continue

        if entity == 1:
            if operation == 1:
                print("call library function to add book")
            elif operation == 2:
                print("call library function to read book")
            elif operation == 3:
                print("call library function to update book")
            elif operation == 4:
                print("call library function to delete book")
        elif entity == 2:
            if operation == 1:
                print("call library function to add user")
            elif operation == 2:
                print("call library function to read user")
            elif operation == 3:
                print("call library function to update user")
            elif operation == 4:
                print("call library function to delete user")
        elif entity == 3:
            if operation == 1:
                print("call library function to issue book to user")
            elif operation == 2:
                print("call library function to return book from user")

        try:        
            print("1 - continue, 2 - exit")
            choice = int(input("Do you want to continue?"))
            if choice == 2:
                break
        except:
            print("invalid input !")
            continue
