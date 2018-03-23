from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.postaldata import PostaldataHelper

class Application:
    def  __init__(self):
        self.wd = webdriver.Firefox(executable_path=r'C:\Users\User\OWASP ZAP\webdriver\windows\64\geckodriver.exe')
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.postaldata = PostaldataHelper(self)



    def destroy(self):
        self.wd.quit()
