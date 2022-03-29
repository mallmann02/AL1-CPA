

def imdb_scrap(html_content):
  soup = BeautifulSoup(html_content, 'html5lib')
  rows = soup.select('table tbody tr')
  field_names = []
  field_values = []

  for row in rows:
    #getting the posters class
    poster_a = row.select('.posterColumn a');
    #selecting image class
    img=poster_a[0].select('img')
    #getting both the redirection url and img source
    href = poster_a[0]['href']
    imgsrc = img[0]['src']

    #class of the title year and such...
    title_class = row.select('.titleColumn a')
    #print(title_class[0].string)
    year_class = row.select('.titleColumn span')
    #print(year_class[0].string.replace('(', '').replace(')', ''))
    rating_class = row.select('.ratingColumn.imdbRating strong')
    print(rating_class[0].string)



imdb = download('https://www.imdb.com/chart/top/')
imdb_scrap(imdb)