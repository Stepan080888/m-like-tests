# -*- coding: utf-8 -*-
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from postaldata import Postaldata


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox(executable_path=r'C:\Users\User\OWASP ZAP\webdriver\windows\64\geckodriver.exe')
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        self.open_home_page()
        self.log_in(username="no_exp2", password="Keplercode344")
        self.open_profile_page()
        self.open_address_page()
        self.open_user_data_form()
        self.fill_in_user_data_form(Postaldata(country="Ukraine", name="Ilyk Stepan", street="Lazarenka str", num_house="23", city="Lviv", state="Lviv reg", zip="82100", phone="0938211673"))
        self.log_out()

    def log_out(self):
        wd = self.wd
        log_out_drop_down = wd.find_element_by_xpath("//*[@id='root']/div/header/div/div/div[3]/div/div/span/div")
        hover = ActionChains(wd).move_to_element(log_out_drop_down)
        hover.perform()
        wd.find_element_by_xpath("//*[@id='root']/div/header/div/div/div[3]/div/div/span/div/div/a").click()
        time.sleep(5)

    def fill_in_user_data_form(self, postaldata):
        wd = self.wd
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

    def log_in(self, username, password):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='root']/div/header/div/div/div[3]/a/button").click()
        wd.find_element_by_id("steamAccountName").click()
        wd.find_element_by_id("steamAccountName").clear()
        wd.find_element_by_id("steamAccountName").send_keys(username)
        wd.find_element_by_id("steamPassword").click()
        wd.find_element_by_id("steamPassword").clear()
        wd.find_element_by_id("steamPassword").send_keys(password)
        wd.find_element_by_id("imageLogin").click()



    def tearDown(self):
        self.wd.quit()
        #self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
