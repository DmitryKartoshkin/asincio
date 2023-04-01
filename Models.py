from sqlalchemy import Column, Integer, JSON, String
# from sqlalchemy.orm import declarative_base
# from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from dsn import engine


Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


class SwapiPeople(Base):
    __tablename__ = "swapi_people"

    # id = Column(Integer, primary_key=True)
    # json = Column(JSON)

    id = Column(Integer, primary_key=True)
    birth_year = Column(String(length=100), nullable=False)
    eye_color = Column(String(length=100), nullable=False)
    films = Column(String(length=100), nullable=False)
    gender = Column(String(length=100), nullable=False)
    hair_color = Column(String(length=100), nullable=False)
    height = Column(String(length=100), nullable=False)
    homeworld = Column(String(length=100), nullable=False)
    mass = Column(String(length=100), nullable=False)
    name = Column(String(length=100), nullable=False)
    skin_color = Column(String(length=100), nullable=False)
    species = Column(String(length=100), nullable=False)
    starships = Column(String(length=100), nullable=False)
    vehicles = Column(String(length=100), nullable=False)


# Base.metadata.create_all(bind=engine)