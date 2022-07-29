import requests
from bs4 import BeautifulSoup


def dad_jokes():
    URL = 'https://www.countryliving.com/life/a27452412/best-dad-jokes/'

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    ff_joke = soup.findAll(class_='body-ul')

    jokelist = []
    for item in ff_joke:
        dad_joke = item.findAll('li')
        for joke in dad_joke:
            jokelist.append(joke.text)
    print(jokelist[0])



if __name__ == '__main__':
    dad_jokes()