import os
from sys import platform
import time

welcome_text = """Welcome to the Father Humor Pip Package Interactive Helper
This guide is designed to automate you through the install process and show you some of the great features of the package
To Get Started, You simply follow the in terminal prompts.
 """


def help_dad():
    #     function to install packages needed before imports

    def install_packages():

        time.sleep(1)
        print(welcome_text)
        time.sleep(1)
        check_for_packages = input('have you installed the required dependancies? (y/n)')

        if check_for_packages == 'y' or check_for_packages == 'Y' or check_for_packages == 'yes' or check_for_packages == 'Yes':
            print(f"""ok you are all set to continue with setup""")
            time.sleep(1.5)
            jokes_loop()
        else:
            print("""that's ok, we will install the required dependancies in order to fully utilize the great features our package offers
                    Standby While the automated system installs the required dependancies......
                            """)
            os.system('pip install bs4')
            os.system('pip install requests')
            print("""
    
                ssssssss
                ss         sss   sss   sssssss   sssssss   sssssss   sssssss   sssssss
                ssssssss   sss   sss   sss       sss       ss        ss        ss
                      ss   sss   sss   ss        ss        sssss     sssssss   sssssss
                      ss   sss   sss   sss       sss       ss             ss        ss
                ssssssss   sssssssss   sssssss   sssssss   sssssss   sssssss   sssssss
                        """)
            time.sleep(2)
            if platform == 'win32':
                os.system('cls')
                time.sleep(1)
                jokes_loop()
            elif platform == 'darwin' or platform == 'linux' or platform == 'linux2':
                os.system('clear')
                time.sleep(1)
                jokes_loop()

        #     function to call imports

    def jokes_loop():
        from pick import pick
        from main import dad_jokes, star_wars, programming
        def loop_jokes():
            time.sleep(1)
            title = 'please select a category of jokes?: '
            options = ['Dad Jokes', 'Star Wars', 'Programming', 'quit']
            option, index = pick(options, title)
            if option == 'Dad Jokes':
                time.sleep(1)
                print(f"""
                **************************************************************
                **************************************************************

                {dad_jokes()}
                **************************************************************
                **************************************************************""")
                loop_jokes()
            elif option == 'Star Wars':
                time.sleep(1)
                print(f"""
                **************************************************************
                **************************************************************

                {star_wars()}
                **************************************************************
                **************************************************************""")
                loop_jokes()

            elif option == 'Programming':
                time.sleep(1)
                print(f"""
                **************************************************************
                **************************************************************

                {programming()}
                **************************************************************
                **************************************************************""")
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

    install_packages()


if __name__ == '__main__':
    help_dad()
