from sqlalchemy import Column, Integer, String
from sql_app.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    fullname = Column(String)
    email = Column(String)
    telp = Column(String)
