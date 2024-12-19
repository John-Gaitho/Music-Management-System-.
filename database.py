from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

DATABASE_URL = "sqlite:///music.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)
