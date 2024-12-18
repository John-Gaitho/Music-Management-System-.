from models import Artist, Album, Track, Session


def create_artist(name):
    session = Session()
    new_artist = Artist(name=name)
    session.add(new_artist)
    session.commit()
    session.close()