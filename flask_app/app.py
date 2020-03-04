# set FLASK_APP=flask_app.app.py
from flask import Flask, request, render_template, jsonify, flash, redirect
from flask_migrate import Migrate
from flask_app.models import db, migrate, Song
#from review.game_service import api



def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tabtadgh:QBYi08LzDfuhX-Ba7fr816wy8RCcv1B5@drona.db.elephantsql.com:5432/tabtadgh'
    #have the db know about the app
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def root():
        return ('Hello World')


    @app.route("/<id>")
    def get_song_data(id=None):
        try:
            x = Song.query.filter(Song.id == id).all()
            x = x[0].__dict__
            del x["_sa_instance_state"]
        
            return jsonify(x)
        except:
            return jsonify({"message": "Song Not Found!"})
    
    
    return app