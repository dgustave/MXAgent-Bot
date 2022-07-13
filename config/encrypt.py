from cryptography.fernet import Fernet
import os, sys
import time


class Encrypts: 
    """
    Encrypts username in password in the bin folder on initial setup. 
    Bin is created upon setup and store secure files in this directory. 
    These files can be overwritten if you rerun the intial setup. 
    """
    def __init__(self): 
        usr = input('Username:')
        self.modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
        if not os.path.exists(f'{self.modpath}/bin/usr/{usr}'):
            self.modloc = os.makedirs(f'{self.modpath}/bin/usr/{usr}') 
        self.modloc = f'{self.modpath}/bin/usr/{usr}'
        time.sleep(1)
        self.keyloc = f'{self.modloc}/key.bin'
        self.secloc = f'{self.modloc}/secure.bin'
    
    def intializer(self,initial_login_info):
        """
        Stores credentials for MXISOAGENT.
        """
        key = Fernet.generate_key()
        with open(self.keyloc, 'wb') as write_key:  
            write_key.write(key)
        cryptoUtil = Fernet(key)
        new = str(initial_login_info)
        encrypted = cryptoUtil.encrypt(new.encode())
        write_key.close()
        
        with open(self.secloc, 'wb') as write_sec:  
            write_sec.write(encrypted)
        write_sec.close()

        with open(self.keyloc, 'rb') as read_key:
                for line in read_key:
                    key1 = line
        read_key.close() 
        
        with open(self.secloc, 'rb') as read_sec:
                for line in read_sec:
                    salt = line
        decrypted = cryptoUtil.decrypt(salt).decode()
        read_sec.close()
        
    def authorize(self):
        """
        Calls credentials to login to MXISOAGENT Automation.
        """
        with open(self.keyloc, 'rb') as key_object:
            for line in key_object:
                key = line
        cryptoUtil = Fernet(key)
        key_object.close()
        with open(self.secloc, 'rb') as sec_object:
            for line in sec_object:
                salt = line
        authorization = cryptoUtil.decrypt(salt).decode()
        sec_object.close()
        return authorization