import numbers
import requests
import os
from bs4 import BeautifulSoup


def dad_jokes(url='https://www.countryliving.com/life/a27452412/best-dad-jokes/'):
    file_path = r'dad_jokes.text'

    jokelist = []
    if os.path.exists(file_path):
        print('file already exists')
    else:
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')
        ff_joke = soup.findAll(class_='body-ul')

        for item in ff_joke:
            dad_joke = item.findAll('li')
            for joke in dad_joke:
                jokelist.append(joke.text)

    # create a file
        with open(file_path, 'w') as fp:
            for joke in jokelist:
                fp.write(joke + '\n')


def star_wars(url='https://www.littledayout.com/star-wars-jokes-puns-use-the-force-for-laughter/'):
    file_path = r'star_wars.text'

    jokelist = []
    if os.path.exists(file_path):
        print('file already exists')
    else:
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')
        sw_joke = soup.findAll(class_='td-post-content tagdiv-type')

        for item in sw_joke:
            star_wars_joke = item.findAll('p')
            for joke in star_wars_joke:
                jokelist.append(joke.text)

    # create a file
        with open(file_path, 'w') as fp:
            for joke in jokelist:
                fp.write(joke + '\n')


def programming(url='https://www.ajokeaday.com/categories/programmer-jokes?page=1'):
    file_path = r'programming.text'

    jokelist = []
    if os.path.exists(file_path):
        print('file already exists')
    else:
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')
        code_joke = soup.findAll(class_='jd-body')

        for item in code_joke:
            programming_joke = item.findAll('p')
            for joke in programming_joke:
                jokelist.append(joke.text)

    # create a file
        with open(file_path, 'w') as fp:
            for joke in jokelist:
                fp.write(joke + '\n')


if __name__ == '__main__':
   programming()


# numbers = range(0,5)
# for num in numbers:
#     num = num + 1
#     print(num)