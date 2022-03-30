def get_data_from_specific_page(url):
    top_250_html = download(url)
    soup = BeautifulSoup(top_250_html, 'html5lib')
    movies_rows = soup.select('.lister-list tr')
    for index, row in enumerate(movies_rows):
        specific_page_path = row.select('.titleColumn a')[0]['href']
        specific_page_url = f'https://www.imdb.com{specific_page_path}'
        specific_page_html = download(specific_page_url)
        selector = BeautifulSoup(specific_page_html, 'html5lib')
        movie_directors_tag = selector.select('.sc-fa02f843-0.fjLeDR > ul > li:first-child a')
        movie_directors_arr = [director.string for director in movie_directors_tag]
        genders_tag = selector.select('.ipc-chip-list.sc-16ede01-4.bMBIRz span')
        genders_arr = [gender.string for gender in genders_tag]
        popularity = selector.select('.sc-edc76a2-1.gopMqI')[0].string
        print(movie_directors_arr, genders_arr, popularity)

get_data_from_specific_page('https://www.imdb.com/chart/top/');  

def imdb_scrap(html_content):
  soup = BeautifulSoup(html_content, 'html5lib')
  rows = soup.select('table tbody tr')

  for row in rows:
    #getting the posters class
    poster_a = row.select('.posterColumn a');
    #selecting image class
    img=poster_a[0].select('img')
    #getting both the redirection url and img source
    poster_url = poster_a[0]['href']
    poster_image = img[0]['src']
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

    field_values = ['title', 'year', 'poster_url',
    'poster_img', 'imdb_rating', 'popularity', 'directors', 'genders']
    


#imdb = download('https://www.imdb.com/chart/top/')
#imdb_scrap(imdb)