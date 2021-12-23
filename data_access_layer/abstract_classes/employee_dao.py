from abc import ABC, abstractmethod

from entities.employee import Employee


class EmployeeDAO(ABC):

    @abstractmethod
    def get_employee_info(self, user: str) -> Employee: # user: str
        pass

    @abstractmethod
    def get_all_employees(self) -> list[Employee]:
        pass

    @abstractmethod
    def update_employee(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def get_login_for_employee(self, user: str, passcode: str):
        pass
