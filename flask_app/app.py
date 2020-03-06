# set FLASK_APP=flask_app.app.py
from flask import Flask, request, render_template, jsonify, flash, redirect
from flask_migrate import Migrate
from flask_app.models import db, migrate, Song
import json
import joblib
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Import Predictive Model
filename = 'Nearest_Neighbors_2.sav'
nn = joblib.load(filename)



def create_app():
    app = Flask(__name__)

    # Connect App to DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tabtadgh:qLJzcc_KrEVBeCdqnhlKayggOHmHolNX@drona.db.elephantsql.com:5432/tabtadgh'
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def root():
        return ('Hello World')

# Decided to use DataFrame Instead of DB
    # @app.route("/<id>")
    # def get_song_data(id=None):
    #     try:
    #         x = Song.query.filter(Song.id == id).all()
    #         x = x[0].__dict__
    #         del x["_sa_instance_state"]
    #         del x["artist_name"]
    #         del x["track_id"]
    #         del x["track_name"]
    #         del x["id"]
    #         del x["duration_ms"]
    #         del x["time_signature"]
    #         del x["popularity"]
    #         x = pd.DataFrame([x], columns=x.keys())
    #         #breakpoint()
    #         predictions = nn.kneighbors(x)[1][0]
    #         predictions = predictions.tolist()
    #         predictions = Song.query.filter(Song.id.in_(predictions))
    #         return jsonify(x)
    #     except:
    #         return jsonify({"message": "Song Not Found!"})

    @app.route("/predict/<id>")
    def get_predictions(id=None):
        '''
        Takes a spotify 'track_id', pulls the related song out of a Dataframe, 
        runs it through a predictive model, and returns suggested songs in JSON format
        '''
        try:
            df = pd.read_csv('http://www.zernach.com/wp-content/uploads/2020/02/SpotifyAudioFeaturesApril2019.csv')
            target   = 'track_id'
            features = ['acousticness',
            'danceability',
            'energy',
            'instrumentalness',
            'key',
            'liveness',
            'loudness',
            'mode',
            'speechiness',
            'tempo',
            'valence'
            ]
            song = df.loc[df['track_id'] == id]
            song = song.iloc[0]['track_id']
            x=[]
            x.append(song)
            track = df[df['track_id'].isin(x)][features]
            predictions      = nn.kneighbors(track)[1][0]
            df_top_similar   = df.iloc[predictions]
            json_top_similar = df_top_similar.to_json(orient='records')
            
            return json_top_similar
        except:
            return jsonify({"message": "Song Not Found!"})

    @app.route("/data/<id>")
    def get_data(id=None):
        '''
        returns JSON song data for given Spotify 'track_id'
        '''
        try:
            spotify = spotipy.Spotify(
                client_credentials_manager=SpotifyClientCredentials(
                    client_id='646dc0908673464f98f0bb00ab896e4d',
                    client_secret='f8541fbcea154850b69b528c995ace80'))
            x = spotify.audio_features(id)
            x = x[0]
            del x["uri"]
            del x["analysis_url"]
            del x["track_href"] 
            del x["type"]
            return jsonify(x)
        except:
            return jsonify({"message": "Song Not Found!"})  

    return app