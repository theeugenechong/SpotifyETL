import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config.playlists import target_playlists

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

my_playlists = spotify.user_playlists('22knflx52v3gsclk5gfdqu3hi', limit=50, offset=0)
# print(my_playlists)

# for playlist in my_playlists['items']:
#     print(playlist)
#     playlist_tracks = spotify.playlist_tracks(playlist['uri'])
#     # print(playlist_tracks)
#     for track in playlist_tracks['items']:
#         if track['track']:
#             print(track['track']['artists'][0]['name'])
#     print(playlist['name'])

tiktok = spotify.playlist_tracks(target_playlists()['viral_hits'])

print(tiktok['items'][0]['track']['uri'])
print(tiktok['items'][0]['track']['album']['release_date'][:4])
print(tiktok['items'][0]['track']['name'])
print(tiktok['items'][0]['track']['artists'][0])
print(type(tiktok['items']))
# for hit in tiktok['items']:
#     print(hit)
#     if hit['track']:
#         print(hit['track']['artists'][0]['name'])

ts = spotify.artist('spotify:artist:06HL4z0CvFAxyc27GXpf02')
print(ts)
print(ts['genres'][0])

drake = spotify.artist('spotify:artist:3TVXtAsR1Inumwj472S9r4')
print(drake)

eilish = spotify.artist('spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH')
print(eilish)