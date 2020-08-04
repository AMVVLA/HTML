import requests
from bs4 import BeautifulSoup
soup_objects = []
base_url= 'https://movie.naver.com/movie/running/current.nhn'
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')
soup_objects.append(soup)

final_data = []
for soup in soup_objects:
    movie_section = soup.select(
        '#wrap > #container > #content > div.article > div.obj_section > div.lst_wrap > ul> li')
    for movie in movie_section:
        a_tag = movie.select_one('dl[class = lst_dsc] > dt[class = tit] > a')

        movie_title = a_tag.contents[0]
        movie_code = a_tag['href'].split('code=')[1]
        movie_data = {'Title':movie_title, 'Code':movie_code}
        final_data.append(movie_data)
print(final_data)