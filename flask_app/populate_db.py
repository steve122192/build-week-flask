import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd 
load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)
cursor = connection.cursor()
print("CURSOR:", cursor)
# query = """
# CREATE TABLE IF NOT EXISTS audio_features (id SERIAL PRIMARY KEY,
# artist_name varchar,
# track_id varchar,
# track_name varchar,
# acousticness float8,
# danceability float8,
# duration_ms int,
# energy float8,
# instrumentalness float8,
# key int,
# liveness float8,
# loudness float8,
# mode int,
# speechiness float8,
# tempo float8,
# time_signature int,
# valence float8,
# popularity int
# );
# """
# cursor.execute(query)
# connection.commit()
df = pd.read_csv("https://raw.githubusercontent.com/mahfuz978/DS-repo/master/SpotifyAudioFeaturesApril2019.csv")
df['track_name'] = df['track_name'].str.replace("'", '')
df['artist_name'] = df['artist_name'].str.replace("'", '')
cursor.execute('DELETE FROM song')

for row in df.itertuples():
    insert_rows = """
    INSERT INTO song
    (artist_name,track_id,track_name,acousticness,danceability,duration_ms,energy,instrumentalness,key,liveness,loudness,mode,speechiness,tempo,time_signature,valence,popularity)
    VALUES """ + "('" + str(row.artist_name) + "', '" + str(row.track_id) + "', '"+ str(row.track_name) + "', "+ str(row.acousticness) + ", " + str(row.danceability) + ', ' + str(row.duration_ms) + ', ' + str(row.energy) + ', ' + str(row.instrumentalness) + ', ' + str(row.key) + ', '+ str(row.liveness) + ', '+ str(row.loudness) + ', '+ str(row.mode) + ', '+ str(row.speechiness) + ', '+ str(row.tempo) + ', ' + str(row.time_signature) + ', ' + str(row.valence) + ', ' + str(row.popularity) + ');'
    cursor.execute(insert_rows)
connection.commit()