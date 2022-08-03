from sys import platform
import time
import random
import re
import os

try:
    import requests
    from bs4 import BeautifulSoup
    from pick import pick


    def dad_jokes(url='https://www.countryliving.com/life/a27452412/best-dad-jokes/'):
        file_path = r'dad_jokes.text'
        jokelist = []

        if os.path.exists(file_path):
            with open('dad_jokes.text') as dj:
                rand_joke = dj.readlines()
                jokelist.append(rand_joke)
            # print(random.choice(rand_joke))
            return random.choice(rand_joke)
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
            # return random.choice(jokelist)
            return jokelist[0]


    def star_wars(url='https://www.menshealth.com/entertainment/a34577665/best-star-wars-jokes/'):
        file_path = r'star_wars.text'
        starwars_jokelist = []
        if os.path.exists(file_path):
            with open('star_wars.text') as sw:
                rand_joke = sw.readlines()
                starwars_jokelist.append(rand_joke)
            return random.choice(rand_joke)

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
            # print(random.choice(starwars_jokelist))
            return starwars_jokelist[0]


    def programming(url='https://betterprogramming.pub/101-funny-programmer-quotes-76c7f335b92d'):
        file_path = r'programming.text'

        prog_jokelist = []
        if os.path.exists(file_path):
            with open('programming.text') as pr:
                rand_joke = pr.readlines()
                prog_jokelist.append(rand_joke)
            return random.choice(rand_joke)
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
            # print(random.choice(prog_jokelist))
            return prog_jokelist[0]

    def helper():
        welcome_text = """Welcome to the Father Humor Pip Package Interactive Helper
    This guide is designed to automate you through the install process and show you some of the great features of the package
    To Get Started, You simply follow the in terminal prompts.
    """
        print(welcome_text)
        def jokes_loop():
            def loop_jokes():
                if platform == 'win32':
                    os.system('cls')
                elif platform == 'darwin' or platform == 'linux' or platform == 'linux2':
                    os.system('clear')
                time.sleep(2)
                title = 'please select a category of jokes?: '
                options = ['Dad Jokes', 'Star Wars', 'Programming', 'quit']
                option, index = pick(options, title)
                if option == 'Dad Jokes':
                    time.sleep(1.5)
                    print(f"""
                    **************************************************************
                    **************************************************************

                    {dad_jokes()}
                    **************************************************************
                    **************************************************************""")
                    time.sleep(4)
                    loop_jokes()
                elif option == 'Star Wars':
                    time.sleep(1.5)
                    print(f"""
                    **************************************************************
                    **************************************************************

                    {star_wars()}
                    **************************************************************
                    **************************************************************""")
                    time.sleep(4)
                    loop_jokes()

                elif option == 'Programming':
                    time.sleep(1.5)
                    print(f"""
                    **************************************************************
                    **************************************************************

                    {programming()}
                    **************************************************************
                    **************************************************************""")
                    time.sleep(4)
                    loop_jokes()

                else:
                    if platform == 'win32':
                        os.system('cls')
                        time.sleep(1)
                        print("""Congratulations!! you have successfully installed the Father Humor PiP package """)
                        return
                    elif platform == 'darwin' or platform == 'linux' or platform == 'linux2':
                        os.system('clear')
                        time.sleep(1)
                        print("""Congratulations!! you have successfully installed the Father Humor PiP package """)
                        return
            loop_jokes()

        if platform == 'win32':
            os.system('cls')
            time.sleep(1)
            jokes_loop()
        elif platform == 'darwin' or platform == 'linux' or platform == 'linux2':
            os.system('clear')
            time.sleep(2)
            jokes_loop()
    helper()
except:
        
        print("""It would appear you do not have the requirements to run this package properly 
            We will install the required dependancies in order to fully utilize the great features our package offers
            Standby While the automated system installs the required dependancies......
            """)

        dependancy_check = input("Would you like to install required dependancies? (N/Y)")
        if dependancy_check == "Y" or dependancy_check == "y":
            time.sleep(5)
            os.system('pip install bs4')
            time.sleep(1)
            os.system('pip install requests')
            time.sleep(1)
            os.system('pip install pick')
            print("""

                        ssssssss
                        ss         sss   sss   sssssss   sssssss   sssssss   sssssss   sssssss
                        ssssssss   sss   sss   sss       sss       ss        ss        ss
                                ss   sss   sss   ss        ss        sssss     sssssss   sssssss
                                ss   sss   sss   sss       sss       ss             ss        ss
                        ssssssss   sssssssss   sssssss   sssssss   sssssss   sssssss   sssssss
                                """)












if __name__ == '__main__':
    # star_wars()
    # programming()
    # dad_jokes()
    helper()
