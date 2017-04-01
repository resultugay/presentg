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
import random

Base = declarative_base()    
engine = create_engine('postgresql://postgres:123456@localhost:5432/test')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Group_member(Base):
    __tablename__ = 'group_members'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    membership_date  = Column(String(1),nullable=False,primary_key=True)
    group_id = Column(String(40), nullable=False) 
    user_id = Column(String(40), nullable=False) 

   
    def __init__(self,group_id,user_id ,membership_date):
        self.group_id = group_id
        self.user_id = user_id
        self.membership_date = membership_date

def get_groups(user_id):
    groups = session.query(Group_member).filter(Group_member.user_id==user_id).all()  if Group_member else None
    return groups

