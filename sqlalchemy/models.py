#!/usr/bin/env python

import arrow
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy_utils import ArrowType

from crud import Base

class Bass(Base):
    __tablename__ = "basses"
    id = Column(Integer, primary_key=True)
    num_strings = Column(Integer)
    make = Column(String)
    has_frets = Column(Boolean)
    created_at = Column(ArrowType(timezone=True), default=arrow.now())

    def __repr__(self):
        return f"<Bass(num_strings='{self.num_strings}', make='{self.make}', has_frets='{self.has_frets}', created_at='{self.created_at}')>"
