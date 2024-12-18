from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import *



class Artist():
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    albums = relationship('Album', back_populates='artist', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Artist(name={self.name})>"
