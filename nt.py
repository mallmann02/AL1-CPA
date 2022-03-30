import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.error import URLError, HTTPError, ContentTooShortError
import re
import csv
import json

def download(url, user_agent='wswp', charset='utf-8'):
  print('Downloading:', url)
  request = urllib.request.Request(url)
  request.add_header('User-agent', user_agent)
  try:
    resp = urllib.request.urlopen(request)
    cs = resp.headers.get_content_charset()
    if not cs:
        cs = charset
    html = resp.read().decode(cs)
  except (URLError, HTTPError, ContentTooShortError) as e:
    print('Download error:', e.reason)
  return html

def cJSON(dl):
  with open('top_250_movies.json', 'w') as f:
    json.dump(dl, f)


  return 0
  

def imdb_scrap(html_content):
  soup = BeautifulSoup(html_content, 'html5lib')
  rows = soup.select('table tbody tr')
  dl = []

  for index,row in enumerate(rows):
    if index == 3:
      break
    #getting the posters class
    poster_a = row.select('.posterColumn a')
    #selecting image class
    img=poster_a[0].select('img')
    #getting both the redirection url and img source
    poster_url = poster_a[0]['href']
    poster_img = img[0]['src']
    #class of the title year and such...
    title_class = row.select('.titleColumn a')
    movie_title = title_class[0].string
    year_class = row.select('.titleColumn span')
    movie_year = year_class[0].string.replace('(', '').replace(')', '')
    rating_class = row.select('.ratingColumn.imdbRating strong')
    movie_rating = rating_class[0].string
    #specific_page_path = row.select('.titleColumn a')[0]['href']
    specific_page_url = f'https://www.imdb.com{poster_url}'
    specific_page_html = download(specific_page_url)
    selector = BeautifulSoup(specific_page_html, 'html5lib')
    movie_directors_tag = selector.select('.sc-fa02f843-0.fjLeDR > ul > li:first-child a')
    movie_directors_arr = [director.string for director in movie_directors_tag]
    genders_tag = selector.select('.ipc-chip-list.sc-16ede01-4.bMBIRz span')
    genders_arr = [gender.string for gender in genders_tag]
    popularity = selector.select('.sc-edc76a2-1.gopMqI')[0].string
    field_values = [movie_title, movie_year, poster_url, poster_img, movie_rating, popularity,
       movie_directors_arr, genders_arr]
    field_names = ['title', 'year', 'poster_url',
    'poster_img', 'imdb_rating', 'popularity', 'directors', 'genders']
    d = dict(zip(field_names, field_values))
    dl.append(d)
  return cJSON(dl)

def run_imdb(url):
  a = download(url)
  return imdb_scrap(a)

run_imdb('https://www.imdb.com/chart/top/')
