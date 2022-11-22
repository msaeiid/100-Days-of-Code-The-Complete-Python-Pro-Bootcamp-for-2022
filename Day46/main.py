from bs4 import BeautifulSoup
import requests
import datetime as dt

URL = "https://www.billboard.com/charts/hot-100/"


def get_date_url():
    date = input("what year you would like to travel to in YYY-MM-DD format.")
    return f"{URL}/{date}/"


def find_100_title(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    tags = soup.findAll(name="h3", class_="a-no-trucate")
    song_title_list = [tag.text.strip() for tag in tags]
    return len(song_title_list) == 100, song_title_list


url = get_date_url()
status, title_list = find_100_title(url)
# spotify doesnt work in Iran
