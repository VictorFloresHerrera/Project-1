#from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class SubmitReimbursement:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_employee_id(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeIdInput")
        return element

    def select_manager_id(self):
        element: WebElement = self.driver.find_element(By.ID, "managerIdInput")
        return element

    def select_reimbursement_amount(self):
        element: WebElement = self.driver.find_element(By.ID, "requestReimbursementInput")
        return element

    def select_reason(self):
        element: WebElement = self.driver.find_element(By.ID, "reasonwhy")
        return element

    def select_submit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "Submitbutton")
        return element
