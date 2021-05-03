#!/usr/bin/env python

from config import DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

engine = create_engine(DATABASE_URI)

Base = declarative_base()

Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def create_database():
    Base.metadata.create_all(engine)

def drop_database():
    Base.metadata.drop_all(engine)

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
