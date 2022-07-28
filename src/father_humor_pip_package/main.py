import requests
from bs4 import BeautifulSoup

URL = 'https://www.countryliving.com/life/a27452412/best-dad-jokes/'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

ff_joke = soup.findAll(class_='body-ul')
# ff_joke = soup.findAll('li')


def get_family_friendly_jokes():
    jokelist = []
    for item in ff_joke:
        jokes = item.text
        print(jokes)


# print(soup)

if __name__ == '__main__':
    get_family_friendly_jokes()