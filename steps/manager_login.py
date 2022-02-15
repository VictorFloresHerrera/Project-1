from behave import Given, When, Then
import time


# Project_One/feature_files/manager_login.feature
@Given(u'the manager is on the login page')
def manager_get_login_page(context):
    context.driver.get(r"C:\Users\itsvi\Desktop\Project1\web_files\html\login.html")


@When(u'the manager enters their userid in the userid input box')
def manager_enter_userid(context):
    context.login_page.select_enter_userid().send_keys("mymanager")


@When(u'the manager enters their passcode in the passcode input box')
def manager_enter_passcode(context):
    context.login_page.select_enter_passcode().send_keys("mycode1")


@When(u'the manager clicks on the Login button')
def manager_click_login(context):
    context.login_page.select_click_login().click()


@Then(u'the manager should be logged in and redirected to the manager home page')
def manager_check_page_url(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Manager Page"
