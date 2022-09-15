from datetime import datetime
import spotipy
import csv
import boto3

from spotipy.oauth2 import SpotifyClientCredentials
from config.playlists import target_playlists
from config.aws import create_bucket, upload_file

HEADERS = ['Year of Release', 'Song Title', 'Artist Name', 'Artist Genre', 'Popularity']
DEFAULT_GENRE = 'dance pop'

BUCKET_NAME = 'spotify-viral-hits-data'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def gather_data(aws=False):
    filepath = 'viral_hits.csv'

    with open(filepath, 'w') as file:
        header = HEADERS
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()

        for target_playlist in target_playlists().keys():
            playlist = spotify.playlist_tracks(target_playlists()[target_playlist])
            write_playlist_tracks_to_csv(writer, playlist)

    if aws:
        date = datetime.now()
        s3_file_name = f'{date.year}/{date.month:02d}/{date.day:02d}/viral_hits.csv'
        upload_file(filepath, BUCKET_NAME, s3_file_name)
            

def write_playlist_tracks_to_csv(csv_writer, playlist):
    for track in playlist['items']:
        if track['track']:
            # obtaining year of release
            release_date = track['track']['album']['release_date']
            year_of_release = release_date[:4]

            # obtaining track title
            song_title = track['track']['name']

            # obtaining artist info
            main_artist = track['track']['artists'][0]
            artist_uri = main_artist['uri']

            artist = spotify.artist(artist_uri)

            artist_name = artist['name']

            # if artist has no genre, their genre is replaced by the default value , dance pop
            main_genre = artist['genres'][0] if artist['genres'] else DEFAULT_GENRE

            # popularity of artist
            popularity = artist['popularity']

            print(f'{year_of_release} - {song_title} - {artist_name} - {main_genre} - {popularity}')

            # write data to csv file
            csv_writer.writerow({
                'Year of Release': year_of_release,
                'Song Title': song_title,
                'Artist Name': artist_name,
                'Artist Genre': main_genre,
                'Popularity': popularity
            })


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    existing_buckets = s3.list_buckets()['Buckets']
    bucket_names = [bucket['Name'] for bucket in existing_buckets]

    if BUCKET_NAME not in bucket_names:
        create_bucket(BUCKET_NAME)

    gather_data(aws=True)


if __name__ == "__main__":
    gather_data(aws=False)