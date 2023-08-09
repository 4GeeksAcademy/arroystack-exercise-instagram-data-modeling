import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    display_name = Column(String(150), nullable=False)
    email = Column(String(320), nullable=False)
    password = Column(String(256), nullable=False) 
    avatar_url = Column(String(	65536), nullable=False) 
   

class Post(Base):
    __tablename__  = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)
    title = Column(String(500), nullable=False)
    body = Column(String(3000), nullable=False)


class Liked_post(Base):
    __tablename__  = "liked_post"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Post)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)


class Media(Base):
    __tablename__  = "media"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Post)
    type = Column(String(150), nullable=False)


class Comment(Base):
    __tablename__  = "comment"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Post)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)


class Follower(Base):
    __tablename__  = "follower"
    id = Column(Integer, primary_key=True)
    followed_to = (Integer, ForeignKey("user.id"))
    followed_by = (Integer, ForeignKey("user.id"))
    user = relationship(User)
    user = relationship(User)






## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
