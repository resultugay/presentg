from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String 
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc

Base = declarative_base()    
engine = create_engine('postgresql://rsltgy:123456@localhost:5432/itu')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class Comment(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    owner_email  = Column(String(40), nullable=False)
    file_id = Column(String(40), nullable=False) 
    comment  = Column(String(40), nullable=False)
    comment_date = Column(String(40), nullable=False)

   
    def __init__(self,owner_email,file_id,comment,comment_date):
        self.owner_email = owner_email
        self.file_id = file_id
        self.comment = comment
        self.comment_date = comment_date


def get_last_3_comments(file_id):
    comments = session.query(Comment).filter(Comment.file_id == file_id).order_by(desc(Comment.comment_date)).limit(3)
    return comments