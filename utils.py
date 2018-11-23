import sqlite3
from movie import Movie

def get_rows(html):
  if html.find_all('table')[3]:
    table = html.find_all('table')[3]
    return table.find_all('tr')[1:]
  else:
    return False

def get_movie_info_list(rows):
  if rows == False:
    return print('Torrent site was not scraped corretly')
  movie_info_list = [Movie(item) for item in rows]
  for movie in movie_info_list:
    print(movie.title, 'info was fetched')
  return movie_info_list

def save_in_database(movie):
  connection = sqlite3.connect('movies.db')
  cursor = connection.cursor()
  
  # Create table
  cursor.execute('CREATE TABLE IF NOT EXISTS movies (id TEXT, title TEXT, rating REAL)')
  # Check if movie existing in db
  cursor.execute('SELECT * FROM movies WHERE id=?', (movie.movie_id, ))
  row = cursor.fetchone()
  
  if row == None:
    cursor.execute("INSERT INTO movies VALUES (?, ?, ?)", (movie.movie_id, movie.title, movie.rating))
    print('Movie "' + movie.title + '" was inserted into DB')
  else:
    print('Movie "' + movie.title + '" already exist. No update made.')
    
  # Commit changes and close connection
  connection.commit()
  cursor.close()

def show_database_entries():
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    for row in cursor.execute('SELECT * FROM movies'):
        print(row)
    connection.close()