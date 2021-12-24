from typing import Text
from sqlalchemy import create_engine, Column
from sqlalchemy.orm import declarative_base
import os
from sqlalchemy.sql.functions import current_timestamp

from sqlalchemy.sql.sqltypes import DATETIME, NUMERIC, TEXT, TIMESTAMP, Float, Integer, String

#create engine
DATABASE_URL = os.getenv("DATABASE_URL") or "sqlite:///finance.db"
DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")
engine = create_engine(DATABASE_URL, echo = True, future = True)

#create vbook table as a metadata

#create users table as a metadata
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, nullable = False)
    username = Column(TEXT, nullable= False)
    hash = Column(TEXT, nullable = False)
    image_register = Column(Integer, nullable = False, default = 10)
    usertype = Column(String, nullable = False , default = "normal")

class Vbook(Base):
    __tablename__ = "vbook"

    id = Column(Integer, primary_key= True, nullable = False)
    word = Column(String(255), nullable = False)
    meaning = Column(String(1023), nullable = False)
    img_url = Column(TEXT, nullable = True)




