from behave import Given, When, Then
import time


@Given(u'The employee is on login page')
def get_login_page(context):
    time.sleep(1)
    context.driver.get(r"C:\Users\itsvi\Desktop\Project1\web_files\html\login.html")


@When(u'The employee enters their userid in the userid input box')
def employee_enters_userid(context):
    time.sleep(1)
    context.login_page.select_enter_userid().send_keys("thisguy")


@When(u'The employee enters their passcode in the passcode input box')
def employee_enters_passcode(context):
    time.sleep(1)
    context.login_page.select_enter_passcode().send_keys("mycode1")


@When(u'The employee clicks on the Login button')
def employee_clicks_submit(context):
    time.sleep(1)
    context.login_page.select_click_login().click()


@Then(u'The employee should be logged in and redirected to the employee home page')
def employee_homepage(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Employee Page"
