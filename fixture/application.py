from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper

class Application:
    def  __init__(self):
        self.wd = webdriver.Firefox(executable_path=r'C:\Users\User\OWASP ZAP\webdriver\windows\64\geckodriver.exe')
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def fill_in_user_data_form(self, postaldata):
        wd = self.wd
        self.open_profile_page()
        self.open_address_page()
        self.open_user_data_form()
        wd.find_element_by_name("rcrs-country").click()
        Select(wd.find_element_by_name("rcrs-country")).select_by_visible_text(postaldata.country)
        wd.find_element_by_xpath("//option[@value='Ukraine']").click()
        wd.find_element_by_xpath("//input[@value='']").click()
        wd.find_element_by_xpath("//input[@value='']").clear()
        wd.find_element_by_xpath("//input[@value='']").send_keys(postaldata.name)
        wd.find_element_by_xpath("//input[@value='']").click()
        wd.find_element_by_xpath("//input[@value='']").clear()
        wd.find_element_by_xpath("//input[@value='']").send_keys(postaldata.street)
        wd.find_element_by_xpath("//input[@value='']").click()
        wd.find_element_by_xpath("//input[@value='']").clear()
        wd.find_element_by_xpath("//input[@value='']").send_keys(postaldata.num_house)
        wd.find_element_by_xpath("//input[@value='']").click()
        wd.find_element_by_xpath("//input[@value='']").clear()
        wd.find_element_by_xpath("//input[@value='']").send_keys(postaldata.city)
        wd.find_element_by_xpath("//input[@value='']").click()
        wd.find_element_by_xpath("//input[@value='']").clear()
        wd.find_element_by_xpath("//input[@value='']").send_keys(postaldata.state)
        wd.find_element_by_xpath("//input[@value='']").click()
        wd.find_element_by_xpath("//input[@value='']").clear()
        wd.find_element_by_xpath("//input[@value='']").send_keys(postaldata.zip)
        wd.find_element_by_xpath("//input[@value='']").click()
        wd.find_element_by_xpath("//input[@value='']").clear()
        wd.find_element_by_xpath("//input[@value='']").send_keys(postaldata.phone)
        wd.find_element_by_xpath("//input[@value='']").click()
        wd.find_element_by_xpath("//input[@value='']").clear()
        wd.find_element_by_xpath("//input[@value='']").send_keys(postaldata.sec_code)
        wd.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[3]/form/div[2]/textarea").click()
        wd.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[3]/form/div[2]/textarea").clear()
        wd.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[3]/form/div[2]/textarea").send_keys(postaldata.address_det)
        wd.find_element_by_xpath("//button[@value='Submit']").click()

    def open_user_data_form(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[3]/div/div/span").click()

    def open_address_page(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/button[3]").click()

    def open_profile_page(self):
        wd = self.wd
        wd.find_element_by_xpath("//img[@alt='User']").click()

    def open_home_page(self):
        wd =self.wd
        wd.get("http://skinstock.gamingdev.io/")

    def destroy(self):
        self.wd.quit()