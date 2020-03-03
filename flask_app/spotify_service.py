import os
import sys
import json
import spotipy
import spotipy.util as util
import webbrowser
from json.decoder import JSONDecodeError
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='646dc0908673464f98f0bb00ab896e4d', client_secret='f8541fbcea154850b69b528c995ace80'))


results = spotify.audio_features('2RM4jf1Xa9zPgMGRDiht8O')
breakpoint()

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])



# CLIENT_ID = '646dc0908673464f98f0bb00ab896e4d'
# CLIENT_SECRET = 'f8541fbcea154850b69b528c995ace80'
# USER_ID = 'steve122192'
# import spotipy.util as util
# uri = 'http://localhost:8888/callback'

# token = util.prompt_for_user_token(USER_ID,
#                                    '',
#                                    client_id=CLIENT_ID,
#                                    client_secret=CLIENT_SECRET,
#                                    redirect_uri=uri)

# scope = 'user-library-read'
# if token:
#     sp        = spotipy.Spotify(auth = token)
#     results   = sp.current_user_saved_tracks()
#     for item in results['items']:
#         track = item['track']
#         print(track['name'] + ' - ' + track['artists'][0]['name'])
# else:
#     print("Can't get token for", username)