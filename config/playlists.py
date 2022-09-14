import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

def target_playlists():
    playlists = {
        'viral_hits': 'spotify:playlist:37i9dQZF1DX2L0iB23Enbq',
        'tiktok_songs_2022': 'spotify:playlist:65LdqYCLcsV0lJoxpeQ6fW'
    }
    return playlists

# def get_artists_from_playlist(playlist_uri):

