"https://zvuk.com/track/65164233"
import requests
from bs4 import BeautifulSoup

req = requests.get("https://rus.hitmotop.com/songs/new")

soup = BeautifulSoup(req.text, 'html.parser')

listOfSongs = []

for i in soup.find_all("div", {"class": "track__img"}, limit=10):
    listOfSongs.append(i['style'][i['style'].find("'")+1:i['style'].rfind("'")])

for ind, i in enumerate(soup.find_all("div",  {"class": "track__info"}, limit=10)):
    print("________________________________________________________________")
    print(i)
    print("INFO NAME")
    print(i.find("div", {"class": "track__title"}).text.strip())
    print(i.find("div", {"class": "track__desc"}).text.strip())
    print(i.find("a", {"class": "track__download-btn"}, href=True)["href"])
    print(i.find("div", {"class": "track__img"}))
    print(listOfSongs[ind])