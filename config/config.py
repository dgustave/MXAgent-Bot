from config.encrypt import Encrypts

   
class Config: 
    def __init__ (self):
        encrypts = Encrypts() 
        reveal = encrypts.authorize() 
        rev = reveal.split()
        self.USERNAME = str(rev[0])
        self.PASSWORD = str(rev[1]) 







