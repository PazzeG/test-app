import requests as r
import json
import os
import psycopg2
from bs4 import BeautifulSoup
from dotenv import load_dotenv

"""
Fonction permettant de récupérer l'URL SensCritique d'un animé
⚠️ Ne pas toucher à cette fonction, elle vous sera utile.
"""
def get_sc_anime_url(anime_name):
    url = f'https://www.senscritique.com/sc2/search/autocomplete.json?query={anime_name}'
    headers = {
        "x-requested-with": "XmlHttpRequest"
    }
    result = r.get(url, headers=headers)
    content_in_json = json.loads(result.content)
    first_result = None
    if len(content_in_json['json']) > 0:
        first_result = content_in_json['json'][0]['url']

    return first_result

load_dotenv()

# take anime's name
anime_Name = input("Entrez le nom de l'anime: ")

# get the url of the anime_Name
anime_url = get_sc_anime_url(anime_Name)

# scraper logic
page = r.get(anime_url)
soup = BeautifulSoup(page.content, 'html.parser')

#find the rating of the anime
sc_rating = soup.find('div', class_="Rating__GlobalRating-sc-1rkvzid-4 fNqmsn").string

conn = None
cur = None

try:
    conn = psycopg2.connect(
        host=os.environ["DATABASE_HOST"],
        port=int(os.environ["DATABASE_PORT"]),
        user=os.environ["DATABASE_USER"],
        password=os.environ["DATABASE_PASSWORD"],
        database=os.environ["DATABASE_NAME"]
    )
    cur = conn.cursor()

    create_ratings_table = """ CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
        CREATE TABLE IF NOT EXISTS ratings (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v1(),
        anime_name VARCHAR(255) NOT NULL,
        anime_rating VARCHAR(255) NOT NULL
    ); """
    cur.execute(create_ratings_table)

    insert_ratings_table = """ INSERT INTO ratings (anime_name, anime_rating) VALUES (%s, %s); """
    cur.execute(insert_ratings_table, (anime_Name, sc_rating))
    conn.commit()
    print(f"{anime_Name} a été ajouté à la base de données")

    
except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL Platform: {e}")
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
