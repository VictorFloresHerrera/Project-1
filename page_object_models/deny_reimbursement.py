# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class DenyReimbursement:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_reimbursement_id(self):
        element: WebElement = self.driver.find_element(By.ID, "ReimbursementIdInput")
        return element

    def select_employee_id(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeIdInput")
        return element

    def select_manager_id(self):
        element: WebElement = self.driver.find_element(By.ID, "managerIdInput")
        return element

    def select_reimbursement(self):
        element: WebElement = self.driver.find_element(By.ID, "requestReimbursementInput")
        return element

    def select_reason(self):
        element: WebElement = self.driver.find_element(By.ID, "reasonwhyinput")
        return element

    def select_approval(self):
        element: WebElement = self.driver.find_element(By.ID, "acceptanceinput")
        return element

    def select_manager_comment(self):
        element: WebElement = self.driver.find_element(By.ID, "managerCommentinput")
        return element

    def select_denied_button(self):
        element: WebElement = self.driver.find_element(By.ID, "Denybutton")
        return element
