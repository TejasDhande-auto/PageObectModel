import allure
from allure_commons.types import AttachmentType
from behave import *
from Pages.LoginPage import LoginPage
from Utilities.customlogger import LogGen
from features import environment
import time

mylogger = LogGen.loggen()


@given(u'Login Page should open')
def step_impl(context):
    environment.invokeloginpage(context)
    time.sleep(5)


@when(u'Enter username "{email}" and password "{password}"')
def step_impl(context, email, password):
    mylogger.info("**** pasring the credentials*******")
    global lpage

    lpage = LoginPage(context.driver)
    time.sleep(5)
    lpage.setusername(email)
    time.sleep(5)
    lpage.setpassword(password)
    time.sleep(5)
    mylogger.info("****Entered Credentials")


@then(u'Click on Login')
def step_impl(context):
    mylogger.info("****Clicling on login button*******")
    lpage.clicklogin()
    time.sleep(5)


@then(u'User should logeed in successfully')
def step_impl(context):
    context.driver.save_screenshot(".\\Screenshots\\" + "Loginpage.png")
    allure.attach(context.driver.get_screenshot_as_png(), name="Login", attachment_type=AttachmentType.PNG)
