import click
from orm import create_artist, create_album, create_track, delete_artist, delete_album, delete_track, get_all_artists, get_all_albums, get_all_tracks, find_artist_by_id, find_album_by_id, find_track_by_id


@click.command()
@click.argument('name')
def create_artist_cli(name):
    create_artist(name)
    click.echo(f"Artist '{name}' has been created successfully!")

@click.command()
@click.argument('artist_id', type=int)
def delete_artist_cli(artist_id):
    delete_artist(artist_id)
    click.echo(f"Artist deleted successfully!")

@click.command()
def list_artists():
    artists = get_all_artists()
    if artists:
        for artist in artists:
            click.echo(f"ID: {artist.id}, Name: {artist.name}")
    else:
        click.echo("No artists found.")    

@click.command()
@click.argument('artist_id', type=int)
def find_artist(artist_id):
    artist = find_artist_by_id(artist_id)
    if artist:
        click.echo(f"Found Artist: {artist.name}")
    else:
        click.echo(f"Artist with ID {artist_id} not found.")

@click.command()                       # Album command.
@click.argument('title')
@click.argument('artist_id', type=int)
def create_album_cli(title, artist_id):
    create_album(title, artist_id)
    click.echo(f"Album '{title}' created successfully for Artist ID {artist_id}!")

@click.command()
@click.argument('album_id', type=int)
def delete_album_cli(album_id):
    delete_album(album_id)
    click.echo(f"Album with ID {album_id} deleted successfully!")

@click.command()
def list_albums():
    albums = get_all_albums()
    if albums:
        for album in albums:
            click.echo(f"ID: {album.id}, Title: {album.title}, Artist: {album.artist.name}")
    else:
        click.echo("No albums found.")

@click.command()
@click.argument('album_id', type=int)
def find_album(album_id):
    album = find_album_by_id(album_id)
    if album:
        click.echo(f"Found Album: {album.title}, Artist: {album.artist.name}")
    else:
        click.echo(f"Album with ID {album_id} not found.")



