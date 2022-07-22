from config.encrypt import Encrypts
from getpass import getpass
import argparse 
import subprocess 
import os,sys
import configparser

config = configparser.ConfigParser()
class Setup:
    #Initialize parser
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.config = config
    def get_arg(self):
        # Adding optional argument
        self.parser.add_argument("-he", "--Helping", action='store_true', 
                            help =
                            """
                            "-u", "--USERNAME", help = "Initialize USER"
                            "-p", "--PASSWORD", help = "Inititalize PASSWORD"
                            "-i", "--Initialize", help = "Add initial username then password"
                            "-e", "--ENV", help = "Add pipenv and run initial requirements.txt"
                            """
                        )
        self.parser.add_argument("-u", "--USERNAME", action='store_true', help = "Initialize USER")
        self.parser.add_argument("-p", "--PASSWORD", action='store_true', help = "Initialize PASSWORD")
        self.parser.add_argument("-i", "--Initialize", action='store_true', help = "Add initial username and password")
        self.parser.add_argument("-e", "--ENV", action='store_true', help = "Add pipenv and run initial requirements.txt")

    def implement_arg(self): 
        default=input("Operating System Name (windows or mac?):")
        args = self.parser.parse_args()
        if default == 'windows':
            sh_lines = ["#!/bin/bash", 
            "python3 -m pip install --upgrade pip", 
            "pipenv install Pipfile"]
            with open(f"{self.modpath}/setup.sh", 'w') as write_sh:  
                write_sh.writelines('\n'.join(sh_lines))
            write_sh.close()
            self.config.read('driver.ini')
            config['DEFAULT']['CHROME_PATH'] = '/drivers/chromedriver.exe'
            config['DEFAULT']['GECKO_PATH'] = '/drivers/geckodriver.exe'
            with open('driver.ini', 'w') as configfile:
                config.write(configfile)
            configfile.close()
        if default == 'mac': 
            sh_lines = ["#!/bin/bash", 
                        "#/bin/bash -c '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'",
                        "#brew install wget",
                        "#brew install --cask anaconda",
                        "brew install --cask chromedriver",
                        "brew install --cask firefox"
                        "python3 -m pip install --upgrade pip", 
                        "pipenv install Pipfile"]
            with open(f"{self.modpath}/setup.sh", 'w') as write_sh:  
                write_sh.writelines('\n'.join(sh_lines))
            write_sh.close()
            self.config.read('driver.ini')
            config['DEFAULT']['USERNAME'] = input('Username:')
            config['DEFAULT']['CHROME_PATH'] = '/opt/homebrew/bin/chromedriver'
            config['DEFAULT']['GECKO_PATH'] = '/opt/homebrew/bin/firefox'
            with open('driver.ini', 'w') as configfile:
                config.write(configfile)
            configfile.close()

        if args.ENV:
            subprocess.call(['sh', 'setup.sh'])
        if args.Initialize: 
            username = config['DEFAULT']['USERNAME']
            password = getpass('Password:')
            login = username +" "+password
            encrypts = Encrypts()
            encrypts.intializer(login)
            print("Begin initial encryption as: % s" % args.Initialize)
        
        if args.USERNAME: 
            reveal = encrypts.authorize() 
            uhalf = reveal.split()
            un = uhalf[0]
            print(un)

        if args.PASSWORD: 
            inquiry = str(input("Are you sure you want to reveal your password? Y/N:"))
            if inquiry == "Y" or inquiry == "y":
                reveal = encrypts.authorize() 
                phalf= reveal.split()
                pswd = phalf[1]
                print(f'The password you have on file is {pswd}')
            elif inquiry == "N" or inquiry == "n":
                print("Thank you for your response")
            else: 
                print("Invalid please try again.")
