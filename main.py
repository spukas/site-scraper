import requests
from bs4 import BeautifulSoup
import config
import utils

session = requests.Session()
# Send request to get cookie from server
session.get(config.lm_url)
# Login to site
session.post(config.lm_url + config.lm_login, data=config.lm_credentials)
# Request html with search results and parse for scraping
response = session.get(config.lm_url + config.lm_search)
soup = BeautifulSoup(response.text, 'html.parser')

## Specify quantity of movies to fetch (from 1 to 50)
html_rows = utils.get_rows(soup, 15)

print('='*10, 'FETCHING MOVIE INFO', '='*10)
movie_list = utils.get_movie_info_list(html_rows)

print('='*10, 'SAVING TO DB', '='*10)
for movie in movie_list:
    utils.save_in_database(movie, session)

print('='*10, 'DB ENTRIES', '='*10)
print(utils.show_database_entries())