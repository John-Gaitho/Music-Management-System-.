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