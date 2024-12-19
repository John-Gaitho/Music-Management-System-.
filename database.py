from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///music_app.db"  #to setup database connection and session.
Base = declarative_base()                 # the base class for models.
engine = create_engine(DATABASE_URL, echo=True)  #to Create the database engine.
Session = sessionmaker(bind=engine)  # Create a configured "Session" class.


Base.metadata.create_all(engine)    # this is to create the tables if they don't exist.  
