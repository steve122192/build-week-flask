import os
import sys
import json
import spotipy
import spotipy.util as util
import webbrowser
from json.decoder import JSONDecodeError
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='646dc0908673464f98f0bb00ab896e4d', client_secret='f8541fbcea154850b69b528c995ace80'))
# results = spotify.audio_features('2RM4jf1Xa9zPgMGRDiht8O')

CLIENT_ID='8b4fcb9d7e7e4841819a7d3c3c3133bc'
CLIENT_SECRET = '4916e108fe6d4ffa8b69b6e73d29eb20'
# USER_ID = 'AN_y0x1vRNadjah88LgzHQ'
USER_ID = 'steve122192'
username = USER_ID
uri = 'http://localhost:8888/callback'
token = util.prompt_for_user_token(USER_ID,
                                     '' ,
                                     client_id=CLIENT_ID,
                                     client_secret=CLIENT_SECRET,
                                     redirect_uri=uri)
spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user('1266247544')
playlists = spotifyObject.('1266247544')
print(playlists)