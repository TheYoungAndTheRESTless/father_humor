import os
from sys import platform


def help_dad():
    # function to run joke selection and functions from scrapers functions
    # variables
    commands_list = ['dad_jokes', 'star_wars_jokes', 'programming_jokes']

    def check_installed_packages():
        check_for_packages = input('have you installed the required dependancies? BS4 and requests? (y/n)')
        if check_for_packages == 'y' or check_for_packages == 'Y' or check_for_packages == 'yes' or check_for_packages == 'Yes':
            print(f"""ok you are all set to continue with setup
        here is a list of joke categories to get started....
        {commands_list[0]}, {commands_list[1]}, {commands_list[2]}""")

        else:
            print("""thats ok, we will install the required dependancies in order to fully utilize the great features our package offers 
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

            print(f"""-----------------------
    ok you are all set to continue with setup
    here is a list of joke categories to get started....
    ----{commands_list[0]}----, {commands_list[1]}----, 
    ----{commands_list[2]}----
    These commands once entered will create a text file with jokes according to the selected category.
    """)
        joke_selection()

    def exit_function():
        exit = input('Would you like to quit the setup or see another joke? (exit/Joke)')
        if exit == 'exit':
            if platform == 'win32':
                os.system('cls')
                print("""Congratulations!! you have successfully installed the Father Humor PiP package """)
            elif platform == 'darwin' or platform == 'linux' or platform == 'linux2':
                os.system('clear')
                print("""Congratulations!! you have successfully installed the Father Humor PiP package """)
            return
        else:
            joke_selection()

    def joke_selection():

        select_jokes = input('Please select from the above joke categories ')
        if select_jokes == 'dad_jokes':
            print(f"""
**************************************************************
**************************************************************

{dad_jokes()}
**************************************************************
**************************************************************""")
            exit_function()
        elif select_jokes == 'star_wars_jokes':
            print(f"""
**************************************************************
**************************************************************

{star_wars()}
**************************************************************
**************************************************************""")
            exit_function()
        elif select_jokes == 'programming_jokes':
            print(f"""
**************************************************************
**************************************************************

{programming()}
**************************************************************
**************************************************************""")
            exit_function()
        else:
            joke_selection()

    welcome_text = """Welcome to the Father Humor Pip Package Interactive Helper
This guide is designed to automate you through the install process and show you some of the great features of the package
To Get Started, You simply follow the in terminal prompts.
 """

    print(welcome_text)
    check_installed_packages()
    from main import dad_jokes, star_wars, programming


if __name__ == '__main__':
    help_dad()
