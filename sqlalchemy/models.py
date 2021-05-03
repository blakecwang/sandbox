#!/usr/bin/env python

import arrow
from sqlalchemy import Column, CheckConstraint, BigInteger, Integer, String, DateTime, Boolean, VARCHAR
from sqlalchemy.dialects.postgresql import MONEY
from sqlalchemy_utils import ArrowType

from crud import Base

class Bass(Base):
    __tablename__ = "basses"
    id = Column(Integer, primary_key=True)
    num_strings = Column(Integer)
    make = Column(String)
    has_frets = Column(Boolean)
    created_at = Column(ArrowType(timezone=True), default=arrow.now())
    price = Column(MONEY)

    def __repr__(self):
        return f"<Bass(num_strings='{self.num_strings}', make='{self.make}', has_frets='{self.has_frets}', created_at='{self.created_at}')>"


class Birth(Base):
    __tablename__ = 'births'
    id = Column(BigInteger, primary_key=True, nullable=False)
    year = Column(VARCHAR(4))
    district_code = Column(Integer)
    district_name = Column(VARCHAR(255))
    neighborhood_code = Column(Integer)
    neighborhood_name = Column(VARCHAR(255))
    gender = Column(
        VARCHAR(255),
        CheckConstraint(
            "gender in ('Boys', 'Girls')",
            "births_gender_check",
        )
    )
    number = Column(Integer)
