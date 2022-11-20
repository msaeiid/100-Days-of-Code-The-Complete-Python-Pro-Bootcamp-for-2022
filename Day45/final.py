from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
links = soup.findAll(name="a", rel="noopener noreferrer")
movie_lst = [links[i].text.split('of')[1].strip() for i in range(len(links) - 1, 0, -1) if
             links[i].text.__contains__(' of ')]

with open('movie_rank.txt', mode='w') as file:
    counter = 0
    for name in movie_lst:
        file.write(f"{counter + 1}) {name}\n")
        counter += 1
