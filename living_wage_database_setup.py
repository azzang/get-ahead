import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import psycopg2

Base = declarative_base()

class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key = True)
    state = Column(String)
    site = Column(String)

class Wages(Base):
    def __init__(self, cells, loc_id):
        for i, v in enumerate('abcdefghijkl'):
            setattr(self, v, cells[i])
        self.loc_id = loc_id
    __tablename__ = 'wages'
    id = Column(Integer, primary_key=True)
    a = Column(Integer)
    b = Column(Integer)
    c = Column(Integer)
    d = Column(Integer)
    e = Column(Integer)
    f = Column(Integer)
    g = Column(Integer)
    h = Column(Integer)
    i = Column(Integer)
    j = Column(Integer)
    k = Column(Integer)
    l = Column(Integer)
    loc_id = Column(Integer, ForeignKey('location.id'))

class Salaries(Base):
    def __init__(self, cells, loc_id):
        for i, v in enumerate('abcdefghijklmnopqrstuv'):
            setattr(self, v, cells[i])
        self.loc_id = loc_id
    __tablename__ = 'salaries'
    id = Column(Integer, primary_key=True)
    a = Column(Integer)
    b = Column(Integer)
    c = Column(Integer)
    d = Column(Integer)
    e = Column(Integer)
    f = Column(Integer)
    g = Column(Integer)
    h = Column(Integer)
    i = Column(Integer)
    j = Column(Integer)
    k = Column(Integer)
    l = Column(Integer)
    m = Column(Integer)
    n = Column(Integer)
    o = Column(Integer)
    p = Column(Integer)
    q = Column(Integer)
    r = Column(Integer)
    s = Column(Integer)
    t = Column(Integer)
    u = Column(Integer)
    v = Column(Integer)
    loc_id = Column(Integer, ForeignKey('location.id'))

engine = create_engine(os.environ.get('DATABASE_URL'))

Base.metadata.create_all(engine)
