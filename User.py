from flask import current_app
from flask_login import UserMixin
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import select
from flask_login import login_manager
import email


Base = declarative_base()    
engine = create_engine('postgresql://postgres:123456@localhost:5432/test')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(40), nullable=False)
    email = Column(String(40), nullable=False)
    name = Column(String(40), nullable=False)
    surname = Column(String(40), nullable=False)
    password = Column(String(40), nullable=False)
    user_id = Column(String(40), nullable=False)
    gender = Column(String(1),nullable=False)
    reg_date = Column(String(40),nullable=False)
    is_active = True
    
    def __init__(self, username,email,name,surname,password,user_id,gender,reg_date):
        self.username = username
        self.email = email
        self.name = name
        self.surname = surname
        self.password = password
        self.user_id = user_id
        self.gender = gender
        self.reg_date = reg_date
        is_active = True

    def get_id(self):
        return self.email
    
    def is_authenticated(self):
        return True
    
    def get_email(self):
        return self.email
    
    def get_user_id(self):
        return self.user_id
       
def get_user(email):
    user1 = session.query(User).filter(User.email==email).first() if User else None
    return user1


def get_username(email):
    user = session.query(User).filter(User.email==email).first() if User else None
    return user.username