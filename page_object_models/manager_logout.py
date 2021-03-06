# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ManagerLogout:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_manager_logout_button(self, logoutbutton):
        element: WebElement = self.driver.find_element(By.ID, logoutbutton)
        return element
