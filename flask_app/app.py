# set FLASK_APP=flask_app.app.py
from flask import Flask, request, render_template, jsonify, flash, redirect
from flask_migrate import Migrate
from flask_app.models import db, migrate, Song
import json
#from review.game_service import api
import joblib
import pandas as pd
filename = 'Nearest_Neighbors_2.sav'
nn = joblib.load(filename)



def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tabtadgh:qLJzcc_KrEVBeCdqnhlKayggOHmHolNX@drona.db.elephantsql.com:5432/tabtadgh'
    #have the db know about the app
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def root():
        return ('Hello World')


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

    @app.route("/df/<id>")
    def get_df_data(id=None):
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
            #json_top_similar = json.loads(df_top_similar.to_json())
            
            return json_top_similar
        except:
            return jsonify({"message": "Song Not Found!"})
            


    
    
    return app