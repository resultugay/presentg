from flask import current_app
from flask_login import UserMixin
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func 
from sqlalchemy.dialects.postgresql import BYTEA
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


class File(Base):
    __tablename__ = 'files'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    group_id = Column(String(40), nullable=False) 
    owner_email  = Column(String(40), nullable=False)
    filename  = Column(String(40), nullable=False)
    file  = Column(BYTEA,nullable=False)
    upload_date = Column(String(40), nullable=False)

   
    def __init__(self,group_id,owner_email ,filename,file,upload_date ):
        self.group_id = group_id
        self.owner_email = owner_email
        self.filename = filename
        self.file = file
        self.upload_date = upload_date

