from config.encrypt import Encrypts
from getpass import getpass
import argparse 
import subprocess 

def setup():
    #Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-he", "--Helping", action='store_true', 
                        help =
                        """
                        "-u", "--USERNAME", help = "Initialize USER"
                        "-p", "--PASSWORD", help = "Inititalize PASSWORD"
                        "-i", "--Initialize", help = "Add initial username then password"
                        "-e", "--ENV", help = "Add pipenv and run initial requirements.txt"
                        """
                    )

    parser.add_argument("-u", "--USERNAME", action='store_true', help = "Initialize USER")
    parser.add_argument("-p", "--PASSWORD", action='store_true', help = "Initialize PASSWORD")
    parser.add_argument("-i", "--Initialize", action='store_true', help = "Add initial username and password")
    parser.add_argument("-e", "--ENV", action='store_true', help = "Add pipenv and run initial requirements.txt")
    args = parser.parse_args()
    encrypts = Encrypts()
    
    if args.ENV:
        subprocess.run(['pipenv', 'install', 'Pipfile']) 
        subprocess.call(['sh', 'setup.sh'])
    if args.Initialize: 
        username = input('Username:')
        password = getpass('Password:')
        login = username +" "+password
        encrypts.intializer(login)
        print("Begin initial encryption as: % s" % args.Initialize)
    
    if args.USERNAME: 
        encrypts = Encrypts() 
        reveal = encrypts.authorize() 
        uhalf = reveal.split()
        un = uhalf[0]
        print(un)

    if args.PASSWORD: 
        inquiry = str(input("Are you sure you want to reveal your password? Y/N:"))
        if inquiry == "Y" or inquiry == "y":
            encrypts = Encrypts() 
            reveal = encrypts.authorize() 
            phalf= reveal.split()
            pswd = phalf[1]
            print(f'The password you have on file is {pswd}')
        elif inquiry == "N" or inquiry == "n":
            print("Thank you for your response")
        else: 
            print("Invalid please try again.")
