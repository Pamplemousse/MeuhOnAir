from bs4 import BeautifulSoup
import requests

def getTracks():
    page = requests.get("http://player.radiomeuh.com/rtdata/tracks10.xml")
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup.select("td.Cell")
