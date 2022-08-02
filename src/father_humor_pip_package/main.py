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
    return jokelist[0]


def star_wars(url='https://www.menshealth.com/entertainment/a34577665/best-star-wars-jokes/'):
    file_path = r'star_wars.text'
    starwars_jokelist = []
    if os.path.exists(file_path):
        print('file already exists')
    else:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        sw_joke = soup.findAll(class_='body-h4')
        # traverse the list of jokes and append to our new list to be used in the text file
        for item in sw_joke:
            star_wars_joke = item.text
            starwars_jokelist.append(star_wars_joke)
        # create a file
        with open(file_path, 'w') as fp:
            for joke in starwars_jokelist:
                fp.write(joke + '\n')
    return starwars_jokelist[0]


def programming(url='https://www.ajokeaday.com/categories/programmer-jokes?page=1'):
    file_path = r'programming.text'

    prog_jokelist = []
    if os.path.exists(file_path):
        print('file already exists')
    else:
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')
        code_joke = soup.findAll(class_='jd-body')

        for item in code_joke:
            programming_joke = item.findAll('p')
            for joke in programming_joke:
                prog_jokelist.append(joke.text)

        # create a file
        with open(file_path, 'w') as fp:
            for joke in prog_jokelist:
                fp.write(joke + '\n')
    return prog_jokelist[0]


if __name__ == '__main__':
    programming()

# numbers = range(0,5)
# for num in numbers:
#     num = num + 1
#     print(num)
