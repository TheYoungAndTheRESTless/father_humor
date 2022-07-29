import requests
import os
from bs4 import BeautifulSoup


def dad_jokes():
    URL = 'https://www.countryliving.com/life/a27452412/best-dad-jokes/'
    file_path = r'src/father_humor_pip_package/dad_jokes.text'

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    ff_joke = soup.findAll(class_='body-ul')

    jokelist = []
    for item in ff_joke:
        dad_joke = item.findAll('li')
        for joke in dad_joke:
            jokelist.append(joke.text)
    print(jokelist[0])

    if os.path.exists(file_path):
        print('file already exists')
    else:
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')
        ff_joke = soup.findAll(class_='body-ul')

        jokelist = []
        for item in ff_joke:
            dad_joke = item.findAll('li')
            for joke in dad_joke:
                jokelist.append(joke.text)

    # create a file
    with open(file_path, 'w') as fp:
        for joke in jokelist:
            fp.write(joke + '\n')

def star_wars():
    URL = 'https://www.littledayout.com/star-wars-jokes-puns-use-the-force-for-laughter/'
    file_path = r'src/father_humor_pip_package/star_wars.text'

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    sw_joke = soup.findAll(class_='td-post-content tagdiv-type')

    jokelist = []
    for item in sw_joke:
        star_wars_joke = item.findAll('p')
        for joke in star_wars_joke:
            jokelist.append(joke.text)
    print(jokelist[0])

    if os.path.exists(file_path):
        print('file already exists')
    else:
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')
        sw_joke = soup.findAll(class_='td-post-content tagdiv-type')

        jokelist = []
        for item in sw_joke:
            star_wars_joke = item.findAll('p')
            for joke in star_wars_joke:
                jokelist.append(joke.text)

    # create a file
    with open(file_path, 'w') as fp:
        for joke in jokelist:
            fp.write(joke + '\n')
            



if __name__ == '__main__':
    star_wars()
