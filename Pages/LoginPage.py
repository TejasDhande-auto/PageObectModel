from selenium import webdriver

class LoginPage:
    username_id = "inputEmailID"
    password_id = "inputPasswordID"
    loginbutton_id = "btnSubmit"

    def __init__(self,driver):
        self.driver = driver

    def setusername(self,username):
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_id(self.loginbutton_id).click()

