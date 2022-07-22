from config.encrypt import Encrypts
import configparser
config = configparser.ConfigParser()

   
class Config: 
    def __init__ (self):
        self.config = config 
        config.read('driver.ini')
        self.chrome = self.config['DEFAULT']['CHROME_PATH']
        self.gecko = self.config['DEFAULT']['GECKO_PATH']
        self.encrypts = Encrypts() 
        reveal = self.encrypts.authorize() 
        rev = reveal.split()
        self.USERNAME = str(rev[0])
        self.PASSWORD = str(rev[1]) 







