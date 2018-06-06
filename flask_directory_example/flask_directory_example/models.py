# models必须创建在项目目录下



from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, UniqueConstraint, Index,DateTime,ForeignKey
from flask_directory_example import db

class Users(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(32),nullable=False,unique=True)
    pwd = Column(String(32),nullable=False)

