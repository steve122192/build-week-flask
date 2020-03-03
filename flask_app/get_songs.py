
import sys
import spotipy
import spotipy.util as util
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

# Grabs some list of saved songs
scope = 'user-library-read'
if token:
    sp        = spotipy.Spotify(auth = token)
    results   = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)
