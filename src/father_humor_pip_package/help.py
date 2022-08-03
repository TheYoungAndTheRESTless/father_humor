import os
from sys import platform
import time

welcome_text = """Welcome to the Father Humor Pip Package Interactive Helper
This guide is designed to automate you through the install process and show you some of the great features of the package
To Get Started, You simply follow the in terminal prompts.
 """


def help_dad():
    time.sleep(1.5)
    print(welcome_text)
    time.sleep(5)
    try:
        from pick import pick
        from scraper import dad_jokes, star_wars, programming

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


    except:
        def install_packages():
            time.sleep(5)
            print("""It would appear you do not have the requirements to run this package properly 
            We will install the required dependancies in order to fully utilize the great features our package offers
            Standby While the automated system installs the required dependancies......
            """)
            time.sleep(1)
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
            help_dad()
        install_packages()


# if __name__ == '__main__':
help_dad()
