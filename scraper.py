import os
import urllib.request
import requests
from bs4 import BeautifulSoup
import re


#Change this to your download directory
OUTPUT_DIR = 'D:\PROJECT\PYTHON'


def getURL(URL):
    try:
        html = requests.get(URL, timeout=5)
        html.raise_for_status()
        soup = BeautifulSoup(html.content, 'lxml')
        return soup
    except requests.exceptions.HTTPError as e:
        print(e)


def getFiles(soup):
    links = soup.find_all("a", attrs={"class": "fileThumb"})
    for link in links:
        href = link.get('href')
        try:
            href = 'http:' + href
            filename = os.path.join(OUTPUT_DIR, href.rsplit('/', 1)[-1])
            print("Downloading %s to %s..." % (href, filename))
            urllib.request.urlretrieve(href, filename)
            print("Done.")
        except urllib.error.URLError as err:
            print("Done downloading all medias")


def main():
    print("Enter the URL of the thread: ")
    bbb = getURL(input())
    getFiles(bbb)


if __name__ == "__main__":
    main()
