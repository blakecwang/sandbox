#!/usr/bin/env python

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, create_engine

# dialect+driver://username:password@host:port/database
DATABASE_URI = "postgres+psycopg2://sandbox:password@localhost:5432/sandbox"
engine = create_engine(DATABASE_URI)

Base = declarative_base()

class bass(Base):
    __tablename__ = "basses"
    id = Column(Integer, primary_key=True)
    num_strings = Column(Integer)
    make = Column(String)
    is_fretless = Column(Boolean)
    created_at = Column(DateTime)

    def __repr__(self):
        return f"<Bass(num_strings='{num_strings}', make='{make}', iis_fretless='{is_fretless}', created_at='{created_at}')>"

Base.metadata.create_all(engine)
