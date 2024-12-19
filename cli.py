import click
from orm import create_artist, create_album, create_track, delete_artist, delete_album, delete_track, get_all_artists, get_all_albums, get_all_tracks, find_artist_by_id, find_album_by_id, find_track_by_id


@click.command()
@click.argument('name')
def create_artist_cli(name):
    create_artist(name)
    click.echo(f"Artist '{name}' has been created successfully!")