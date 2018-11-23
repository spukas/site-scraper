import requests
from bs4 import BeautifulSoup
import config
import utils

session = requests.Session()
session.get(config.lm_url)
session.post(config.lm_url + config.lm_login, data=config.lm_credentials)
response = session.get(config.lm_url + config.lm_search)
soup = BeautifulSoup(response.text, 'html.parser')

html_rows = utils.get_rows(soup)[0:5]

print('='*10, 'FETCHING MOVIE INFO', '='*10)
movie_list = utils.get_movie_info_list(html_rows)

print('='*10, 'SAVING TO DB', '='*10)
for movie in movie_list:
    utils.save_in_database(movie)

print('='*10, 'DB ENTRIES', '='*10)
print(utils.show_database_entries())