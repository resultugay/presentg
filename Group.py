from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base()    
engine = create_engine('postgresql://postgres:123456@localhost:5432/test')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Group(Base):
    __tablename__ = 'groups'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    group_id = Column(String(40), nullable=False) 
    group_name  = Column(String(40), nullable=False)
    creation_date  = Column(String(40),nullable=False)
    creator_email = Column(String(40), nullable=False)

   
    def __init__(self,group_id,group_name ,creation_date,creator_email ):
        self.group_id = group_id
        self.group_name = group_name
        self.creation_date = creation_date
        self.creator_email = creator_email


def get_group(group_name):
    group1 = session.query(Group).filter(Group.group_name==group_name).first() if Group else None
    return group1

def get_group2(group_name):
    group1 = session.query(Group).filter(Group.group_name==group_name)
    return group1
def get_group_using_group_id(group_id):
    group1 = session.query(Group).filter(Group.group_id==group_id).first()
    return group1