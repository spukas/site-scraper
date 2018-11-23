# LM torrent site scraper and .torrent file downloader

Python script to scrape LinkoManija.net torrent site.

**Features**
* scrape torrent site to get most popular movies
* fetch movie info from OMDB and save it into SQLite database
* download .torrent file and save to disk

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

Clone this repo, create virtual environment and install packages from `rquiretiments.txt` file by running following commands in your terminal

```python=
git clone https://github.com/spukas/site-scraper.git
python3 -m venv site-scraper
pip install -r requirements.txt 
```

## Usage

From your Terminal run `python3 main.py`
In the Terminal you will get info:

- Which movies was fetched
- Which ones were saved into the DB
- Movies will not duplicate and will be carefuly filtered
- Which movie `.torrent` files were downloaded

In the cloned project directory you will see newly created `/torrent/` folder, where downloaded torrent files will be saved and `movie.db` where fetched movie info will be saved. 

Feel free to modify function `utils.get_rows(soup, 15)` in `main.py` file by setting number of movies to fetch as the second argument of the function.