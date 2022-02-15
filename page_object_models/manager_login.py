# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ManagerLogin:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_enter_userid(self):
        element: WebElement = self.driver.find_element(By.ID, "userid")
        return element

    def select_enter_passcode(self):
        element: WebElement = self.driver.find_element(By.ID, "passcode")
        return element

    def select_click_login(self):
        element: WebElement = self.driver.find_element(By.ID, "button")
        return element
