from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import Config
import os,sys
import time
from logs import Logger

start_time = time.time()
logger = Logger()
conf = Config()
USERNAME = conf.USERNAME
PASSWORD = conf.PASSWORD 


class Mxisoagent: 
    """
    Automated bot that resave accounts on MXAISOagent. 
    Credentials should already be in the system. 
    Default is set to Chrome, another option is to set to Firefox all lowercase.
    """
    def __init__(self, default='chrome', window='show'):
        self.window = str(window).lower()
        self.default = str(default).lower()
        self.logger = logger
        self.start_time = start_time
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD 
        self.modpath = str(os.getcwd())
        self.datapath = f'{self.modpath}/data'
        print(self.datapath)
        self.loginAttempts = 0 
        self.modal_popups = 0
        if self.default == 'chrome':
            self.chrome_driver_path = conf.chrome
            if self.window == 'show': 
                self.driver = webdriver.Chrome(self.chrome_driver_path)
                self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                self.driver.maximize_window()
            elif self.window == 'hide':
                chrome_options = Options()
                chrome_options.add_argument("--disable-extensions")
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--headless")
                self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path, options=chrome_options)
                self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        if self.default == 'firefox': 
            self.firefox_driver_path = conf.gecko
            if self.window == 'show': 
                self.driver = webdriver.Firefox(executable_path=self.firefox_driver_path)
                self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                self.driver.maximize_window()
            elif self.window == 'hide': 
                options = webdriver.FirefoxOptions()
                options.headless = True
                self.driver = webdriver.Firefox(executable_path=self.firefox_driver_path, options=options)
                self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                        
    def initiator(self): 
        """
        Web link is set to MXISOAGENT 
        """
        self.driver.get('https://mxisoagent.com/mx/login.aspx')
    def signin_check(self):
        """
        Check to see if you are already signed in to prevent lockouts. 
        """
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[1]/td/div[1]/div/div[3]/input[1]'))).send_keys(mid)
            WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[1]/td/div[1]/div/div[3]/input[2]'))).click()
            print("MXISOAGENT: sign on complete.")
            return True
        except:
            return False
    def popups(self):
        """
        Was made to handle and exit special handling notes. 
        """
        try:
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "divSpecialHandling")))
            WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[2]/td/div[2]/form/div[9]/table/tbody/tr/td/div[1]/div[2]/div[1]/div/div/div[2]/div/table/tbody/tr[2]/td/div/a"))).click()
            self.modal_popups += 1
        except:
            pass
    def signOn(self):
        """
        Max attempts is set to 4 tries due to MXA having down time. 
        Logs in using credentials from secure bin. 
        """
        if self.loginAttempts < 4:
            self.popups()
            try: 
                isSignedIn = self.signin_check()
                if isSignedIn == True:
                    return
                elif isSignedIn == False:
                    try:
                        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'LoginSection')))
                        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div/p[1]/input'))).send_keys(USERNAME)
                        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div/p[2]/input'))).send_keys(PASSWORD)
                        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/div/p[3]/input'))).click()
                        if isSignedIn == True:
                            return
                        elif isSignedIn == False:
                            self.loginAttempts += 1
                            self.signOn() 
                    except:
                        self.loginAttempts += 1
                        self.signOn() 
            except:
                self.loginAttempts += 1
                self.signOn() 
        else: 
          print("MXISOAGENT: sign in is not successful")  
    def resave(self, filename = input("Please type in filename (only .csv filetypes are accepted):")):
        """
        Need specific filename for .csv extenstions only. This was setup to use download from MXA partner/portfolio merchants only. 
        At minimum a csv can be created with the column name XMID. 
        Please store in data external. 
        Processed in the data folder is generated if some MIDS were not found please recheck these accounts. If working properly underwriting will need to review these accounts. 

        """
        if os.path.exists(f'{self.datapath}/external/{filename}.csv'): 
            filepath = f'{self.datapath}/external/{filename}.csv'
            df = pd.read_csv(f'{self.datapath}/external/{filename}.csv')
            print(filepath)
        elif filename.endswith('.csv'):
            if os.path.exists(f'{self.datapath}/external/{filename}'): 
                df = pd.read_csv(f'{self.datapath}/external/{filename}')
            else: 
                filepath = f'{self.datapath}/external/{filename}'
                return print(f"Please add csv file to data/external directory or check for spelling errors in filename for {filepath}")
        else: 
            return print("Please add to data external or check for spelling errors in filename")
        under_review = []
        mid_nan = float('nan')
        for x, row in df.iterrows(): 
            try: 
                mid = str(int(row.XMID))
                WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[1]/td/div[1]/div/div[3]/input[1]'))).send_keys(mid)
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[1]/td/div[1]/div/div[3]/input[2]'))).click()
                WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td/div[2]/form/div[9]/div[1]/div/table/tbody/tr/td[2]/a'))).click()
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td/div[2]/form/div[9]/table/tbody/tr/td/div[1]/div[5]/table/tbody/tr/td[3]/div'))).click()
            except Exception as e:
                if mid != mid_nan: 
                    under_review.append(mid)
                    self.popups()
                    try: 
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[2]/td/div[2]/form/div[9]/table/tbody/tr/td/div[1]/div[5]/table/tbody/tr/td[3]/div'))).click()
                        
                    except:
                        pass
                pass
            finally: 
                self.driver.back()
                time.sleep(4)
        self.driver.quit()
        underwriting_df = pd.DataFrame(under_review)
        if underwriting_df.empty == True: 
            pass 
        else: 
            underwriting_df.to_csv(f'{self.datapath}/processed/{filename}_underwriting_mids_review.csv', index=False)
            self.logger.info(f"Login Attempts: {self.loginAttempts} Popups: {self.modal_popups} Runtime: {(time.time() - self.start_time)}")
        

if __name__ == '__main__':
    mxa = Mxisoagent()
    mxa.initiator()
    mxa.signOn()
    mxa.resave()
    print("All contents of the csv have successfully pumped over to Mxconnect")