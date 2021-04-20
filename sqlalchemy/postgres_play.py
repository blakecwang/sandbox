#!/usr/bin/env python

# You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".

from sqlalchemy import create_engine

DATABASE_URI = "postgres+psycopg2://postgres:password@localhost:5432/basses"
engine = create_engine(DATABASE_URI)
