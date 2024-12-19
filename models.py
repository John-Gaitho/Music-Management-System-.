from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Artist(Base):
    __tablename__ = 'artists'      # to specify the name of table in db.

    id = Column(Integer, primary_key=True)    # to define a column id which is an integer.
    name = Column(String, nullable=False)     # for name which cannot be null.

    albums = relationship('Album', back_populates='artist', cascade='all, delete-orphan') # to delete all related albs when artist is deleted.

    def __repr__(self):
        return f"<Artist(name={self.name})>"

class Album(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    artist_id = Column(Integer, ForeignKey('artists.id'))

    artist = relationship('Artist', back_populates='albums')                             # a two way relashionship btn album & artist.
    tracks = relationship('Track', back_populates='album', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Album(title={self.title}, artist={self.artist.name})>"

class Track(Base):
    __tablename__ = 'tracks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    album_id = Column(Integer, ForeignKey('albums.id'))  #to link each track to an album. 

    album = relationship('Album', back_populates='tracks') 

    def __repr__(self):
        return f"<Track(title={self.title}, album={self.album.title})>"

DATABASE_URL = "sqlite:///music.db"
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
