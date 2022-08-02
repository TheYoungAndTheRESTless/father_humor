import requests
import os
from bs4 import BeautifulSoup
import random
import re


def dad_jokes(url='https://www.countryliving.com/life/a27452412/best-dad-jokes/'):
    file_path = r'dad_jokes.text'
    jokelist = []

    if os.path.exists(file_path):
        with open('dad_jokes.text') as dj:
            rand_joke = dj.readlines()
            jokelist.append(rand_joke)
        print(random.choice(rand_joke))
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
        with open('star_wars.text') as sw:
            rand_joke = sw.readlines()
            starwars_jokelist.append(rand_joke)
        print(random.choice(rand_joke))
    else:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        sw_joke = soup.findAll(class_='body-h4')
        for item in sw_joke:
            star_wars_joke = item.text
            starwars_jokelist.append(star_wars_joke)
        # create a file
        with open(file_path, 'w') as fp:
            for joke in starwars_jokelist:
                fp.write(joke + '\n')
    return starwars_jokelist[0]


def programming(url='https://betterprogramming.pub/101-funny-programmer-quotes-76c7f335b92d'):
    file_path = r'programming.text'

    prog_jokelist = []
    if os.path.exists(file_path):
        with open('programming.text') as pr:
            rand_joke = pr.readlines()
            prog_jokelist.append(rand_joke)
        print(random.choice(rand_joke))
    else:
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')
        code_joke = soup.findAll('li')

        for item in code_joke:
            programming_joke = item.text
            prog_jokelist.append(programming_joke)

        # create a file
        with open(file_path, 'w') as fp:
            for joke in prog_jokelist:
                text = re.sub("\D(source)\D", '', joke)
                fp.write(text + '\n')
    return prog_jokelist[0]


if __name__ == '__main__':
    star_wars()
    programming()
    dad_jokes()

