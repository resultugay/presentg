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


Base = declarative_base()    
engine = create_engine('postgresql://postgres:123456@localhost:5432/test')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class user(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(40), nullable=False)
    email = Column(String(40), nullable=False)
    name = Column(String(40), nullable=False)
    surname = Column(String(40), nullable=False)
    password = Column(String(40), nullable=False)
    salt = Column(String(40), nullable=False)
    gender = Column(String(1),nullable=False)
    is_active = True
    
    def __init__(self, username,email,name,surname,password,salt,gender):
        self.username = username
        self.email = email
        self.name = name
        self.surname = surname
        self.password = password
        self.salt = salt
        self.gender = gender
        self.active = True
        self.is_admin = False
        
    def get_id(self):
        return self.username

    def is_authenticated(self):
        return True

def get_user(username):
    user1 = session.query(user).filter(user.username==username).first() if user else None
    return user1