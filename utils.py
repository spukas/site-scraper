import sqlite3
import requests
import os
from movie import Movie
import config

def get_rows(html, quantity):
  if html.find_all('table')[3]:
    table = html.find_all('table')[3]
    rows = table.find_all('tr')[1:]
    return rows[:quantity]
  else:
    return False

def get_movie_info_list(rows):
  if rows == False:
    return print('Torrent site was not scraped corretly')
  movie_info_list = [Movie(item) for item in rows]
  for movie in movie_info_list:
    print(movie.title, 'info was fetched')
  return movie_info_list

def save_in_database(movie, session):
  connection = sqlite3.connect('movies.db')
  cursor = connection.cursor()
  
  # Create table
  cursor.execute('CREATE TABLE IF NOT EXISTS movies (id TEXT, title TEXT, rating REAL)')
  # Check if movie existing in db
  cursor.execute('SELECT * FROM movies WHERE id=?', (movie.movie_id, ))
  row = cursor.fetchone()
  
  # If movie not in DB then add and download torrent file
  if row == None:
    cursor.execute("INSERT INTO movies VALUES (?, ?, ?)", (movie.movie_id, movie.title, movie.rating))
    print('Movie "' + movie.title + '" added')
    url = config.lm_url + movie.torrent
    save_torrent(url, session);
  else:
    print('Movie "' + movie.title + '" already exist')
    
  # Commit changes and close connection
  connection.commit()
  cursor.close()

def show_database_entries():
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    for row in cursor.execute('SELECT * FROM movies'):
        print(row)
    connection.close()

def save_torrent(url, session):
    response = session.get(url)
    save_location = os.getcwd() + '/torrents/'
    filename = save_location + url.split('name=')[1]
    # Creates new directory if the directory does not exist. Otherwise, just use the existing path.
    if not os.path.isdir(save_location):
        os.mkdir(save_location)
    with open(filename, 'wb') as file:
        file.write(response.content)
        print('Torrent downloaded')
    file.close()