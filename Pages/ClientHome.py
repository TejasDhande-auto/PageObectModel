from selenium import webdriver
class ClientHome:
    joinsession_xpath = ""
    addnote_xpath = ""
    editnote_xpath= ""
    activeactivity_xpath = ""
    archievedactivity_xpath = ""
    chatentertext_xpath = ""
    chatsend_xoath= ""
    
    def __init__(self,driver):
        self.driver = driver

    def NextSession(self):
        self.driver.find_element_by_id("").send_keys()

    def Notes(self):
        self.driver.find_element_by_id("").send_Keys()

    def ActivitiesHome(self):
        self.driver.find_element_by_id("").send_Keys()

    def RecommendedonNetQ(self):
        self.driver.find_element_by_id("").send_Keys()

    def ClientChat(self):
        self.driver.find_element_by_id("").send_Keys()
