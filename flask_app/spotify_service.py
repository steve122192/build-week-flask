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

​
​
# User ID: steve122192
CLIENT_ID='646dc0908673464f98f0bb00ab896e4d'
CLIENT_SECRET = 'f8541fbcea154850b69b528c995ace80'
USER_ID = 'steve122192'
username = USER_ID
uri = 'http://google.com/'
​
​
token = util.prompt_for_user_token(USER_ID,
                                     '' ,
                                     client_id=CLIENT_ID,
                                     client_secret=CLIENT_SECRET,
                                     redirect_uri=uri)
​
spotifyObject = spotipy.Spotify(auth=token)
​
user = spotifyObject.current_user()
​
# # print(json.dumps(user, sort_keys=True, indent=4))
# ​
# displayName = user['display_name']
# followers = user['followers']['total']
# ​
# while True:
# ​
#     print()
#     print(">>>>> Welcome to Spotify" + displayName + "!")
#     print("you have" + str(followers) + " followers.")
#     print()
#     print("0 - Search for an artist")
#     print("1 - exit")
#     print()
#     choice = input("Your choice: ")
# ​
#     if choice == '0':
#         print()
#         searchQuery = input("Ok, what's their name?: ")
#         print()
# ​
#         searchResults = spotifyObject.search(searchQuery, 1, 0, 'artist')
#         # print(json.dumps(searchResults, sort_keys=True, indent=4))
#         artist = searchResults['artists']['items'][0]
#         print(artist['name'])
#         print(str(artist['followers']['total']) + ' followers')
#         print(artist['genres'][0])
#         print()
#         webbrowser.open(artist['images'][0]['url'])
#         artistID = artist['id']
# ​
#         trackURIs = []
#         trackArt = []
#         z = 0
# ​
#         albumResults = spotifyObject.artist_albums(artistID)
#         albumResults = albumResults['items']
# ​
#         for item in albumResults:
#             print('ALBUM ' + item['name'])
#             albumID = item['id']
#             albumArt = item['images'][0]['url']
# ​
#             trackResults = spotifyObject.album_tracks(albumID)
#             trackResults = trackResults['items']
# ​
#             for item in trackResults:
#                 print(str(z) + ': ' + item['name'])
#                 trackURIs.append(item['uri'])
#                 trackArt.append(albumArt)
#                 z+=1
#             print()
# ​
#         while True:
#             songSelection = input('Enter a song number to see the album art: ')
#             if songSelection == 'x':
#                 break
#             webbrowser.open(trackArt[int(songSelection)])
# ​
# ​
​
​
    # if choice == '1':
    #     break
​
# export SPOTIPY_CLIENT_ID='2b8d0ff261044e70a5178d2c347aef4a'
# export SPOTIPY_CLIENT_SECRET='3f4705db2f8646a4a18f64676701aeec'
# export SPOTIPY_URI='http://google.com/'