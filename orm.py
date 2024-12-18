from models import Artist, Album, Track, Session


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
    session = Session()
    artist = session.query(Artist).get(artist_id)
    session.close()
    return artist

def create_album(title, artist_id):
    Session = Session()
    artist = Session.query(Artist).get(artist_id)
    if artist:
        new_album = Album(title=title, artist_id=artist.id)
        Session.add(new_album)
        Session.commit()
        Session.close()
    else:
        print(f"Artist with ID {artist_id} not found.")

def delete_albulm(album_id):
    Session = Session() 
    album = Session.query(Album).get(album_id)
    if album:
        Session.delete(album)
        Session.commit()
        Session.close()
    else:
        print(f"Album with ID {album_id} not found.")

def find_albulm_by_id(album_id):
    Session = Session() 
    album = Session.query(Album).get(album_id)
    Session.close() 
    return album
      
