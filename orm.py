from models import Artist, Album, Track
from database import Session

def create_artist(name):
    session = Session() 
    new_artist = Artist(name=name)
    session.add(new_artist)
    session.commit()
    session.close()

def delete_artist(artist_id):
    session = Session() 
    artist = session.query(Artist).get(artist_id)
    if artist:
        session.delete(artist)
        session.commit()
        session.close()
    else:
        print(f"Artist with ID {artist_id} not found.")

def get_all_artists():
    session = Session()  
    artists = session.query(Artist).all()
    session.close()
    return artists

def find_artist_by_id(artist_id):
    session = Session()  # Use session
    artist = session.query(Artist).get(artist_id)
    session.close()
    return artist

def create_album(title, artist_id):
    session = Session()  # Use session
    artist = session.query(Artist).get(artist_id)
    if artist:
        new_album = Album(title=title, artist_id=artist.id)
        session.add(new_album)
        session.commit()
        session.close()
    else:
        print(f"Artist with ID {artist_id} not found.")

def delete_album(album_id):
    session = Session()  # Use session
    album = session.query(Album).get(album_id)
    if album:
        session.delete(album)
        session.commit()
        session.close()
    else:
        print(f"Album with ID {album_id} not found.")

def get_all_albums():
    session = Session()  # Use session
    albums = session.query(Album).all()
    session.close()
    return albums

def find_album_by_id(album_id):
    session = Session()  # Use session
    album = session.query(Album).get(album_id)
    session.close() 
    return album

def create_track(title, album_id):
    session = Session()  # Use session
    album = session.query(Album).get(album_id)
    if album:
        new_track = Track(title=title, album_id=album.id)
        session.add(new_track)
        session.commit()
        session.close()
    else:
        print(f"Album with ID {album_id} not found.")

def delete_track(track_id):
    session = Session()  # Use session
    track = session.query(Track).get(track_id)
    if track:
        session.delete(track)
        session.commit()
        session.close()
    else:
        print(f"Track with ID {track_id} not found.")

def get_all_tracks():
    session = Session()  # Use session
    tracks = session.query(Track).all()
    session.close()
    return tracks

def find_track_by_id(track_id):
    session = Session()  # Use session
    track = session.query(Track).get(track_id)
    session.close()
    return track
