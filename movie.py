import requests
import json
from guessit import guessit
import config

class Movie:
  def __init__(self, data):
    self.set_torrent(data)
    self.set_search_title()
    self.set_omdb_link()
    self.set_movie_info()
    
  def set_torrent(self, data):
    torrent = ''
    for item in data.find_all('a', class_="index"):
      torrent = item.get('href')
    self.torrent = torrent

  def set_search_title(self):
    torrent_title = self.torrent.split('name=')[1].replace('%20', '.')
    clean_title = guessit(torrent_title)['title']
    self.search_title = clean_title.replace(' ', '+')

  def set_omdb_link(self):
    self.omdb_link = config.omdb_url + self.search_title + config.omdb_api

  def set_movie_info(self):
    response = requests.get(self.omdb_link)
    info = json.loads(response.text)
    self.movie_info = info
    self.movie_id = info['imdbID']
    self.title = info['Title']
    self.rating = float(info['imdbRating'])