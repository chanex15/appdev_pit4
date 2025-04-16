import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()


SQLALCHEMY_DATABASE_URL = "postgresql://pit4db_user:wTz0uYm22dOAOx512qiEbpg0ZeLJPbFG@dpg-cvvgd03uibrs73beebh0-a.virginia-postgres.render.com/pit4db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
