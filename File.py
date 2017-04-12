from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String 
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
    file_id = Column(String(40), nullable=False) 
    owner_email  = Column(String(40), nullable=False)
    filename  = Column(String(40), nullable=False)
    file  = Column(BYTEA,nullable=False)
    upload_date = Column(String(40), nullable=False)

   
    def __init__(self,group_id,file_id,owner_email ,filename,file,upload_date ):
        self.group_id = group_id
        self.file_id = file_id
        self.owner_email = owner_email
        self.filename = filename
        self.file = file
        self.upload_date = upload_date

def get_file_names_using_group_id(group_id):
    file = session.query(File.file_id,File.filename).filter(File.group_id==group_id)
    files = {}
    for k,v in file:
        files[k] = v
    return files

def get_file_using_file_id(file_id):
    file = session.query(File).filter(File.file_id==file_id).first()
    return file