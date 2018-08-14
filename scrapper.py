from bs4 import BeautifulSoup
import requests


def getTracks():
    page = requests.get("http://player.radiomeuh.com/rtdata/tracks10.xml")
    soup = BeautifulSoup(page.content, 'html.parser')

    tds = soup.select("td.Cell")
    return reversed(tds)
