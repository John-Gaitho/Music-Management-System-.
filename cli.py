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