import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

def target_playlists():
    playlists = {
        'viral_hits': 'spotify:playlist:37i9dQZF1DX2L0iB23Enbq'
    }
    return playlists
