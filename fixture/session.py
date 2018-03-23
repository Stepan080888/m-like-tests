from selenium.webdriver.common.action_chains import ActionChains
import time

class SessionHelper:
    def __init__(self, app):
        self.app = app


    def log_in(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//div[@id='root']/div/header/div/div/div[3]/a/button").click()
        wd.find_element_by_id("steamAccountName").click()
        wd.find_element_by_id("steamAccountName").clear()
        wd.find_element_by_id("steamAccountName").send_keys(username)
        wd.find_element_by_id("steamPassword").click()
        wd.find_element_by_id("steamPassword").clear()
        wd.find_element_by_id("steamPassword").send_keys(password)
        wd.find_element_by_id("imageLogin").click()

    def log_out(self):
        wd = self.app.wd
        log_out_drop_down = wd.find_element_by_xpath("//*[@id='root']/div/header/div/div/div[3]/div/div/span/div")
        hover = ActionChains(wd).move_to_element(log_out_drop_down)
        hover.perform()
        wd.find_element_by_xpath("//*[@id='root']/div/header/div/div/div[3]/div/div/span/div/div/a").click()
        wd.find_element_by_xpath("//*[@id='root']/div/header/div/div/div[3]/a/button").click()
        wd.find_element_by_xpath("//*[@id='openidForm']/div/div[1]/div[3]/a").click()
        time.sleep(5)

