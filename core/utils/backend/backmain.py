"https://zvuk.com/track/65164233"
import requests
from bs4 import BeautifulSoup

class Recommendation:
    def __init__(self, amount):
        req = requests.get("https://rus.hitmotop.com/songs/new")

        self.amount = amount

        self.soup = BeautifulSoup(req.text, 'html.parser')

        self.listOfSongs = []

        for i in self.soup.find_all("div", {"class": "track__img"}, limit=self.amount):
            self.listOfSongs.append([i['style'][i['style'].find("'") + 1:i['style'].rfind("'")]])

        for ind, i in enumerate(self.soup.find_all("div", {"class": "track__info"}, limit=self.amount)):
            # print("________________________________________________________________")
            # print(i)
            # print("INFO NAME")
            # print(i.find("div", {"class": "track__title"}).text.strip())
            # print(i.find("div", {"class": "track__desc"}).text.strip())
            # print(i.find("a", {"class": "track__download-btn"}, href=True)["href"])
            # print(i.find("div", {"class": "track__img"}))
            # print(self.listOfSongs[ind])
            self.listOfSongs[ind].append([i.find("div", {"class": "track__title"}).text.strip(),
                                          i.find("div", {"class": "track__desc"}).text.strip(),
                                          i.find("a", {"class": "track__download-btn"}, href=True)["href"]])

if __name__ == "__main__":
    recommendation = Recommendation(15)
    print(recommendation.listOfSongs)