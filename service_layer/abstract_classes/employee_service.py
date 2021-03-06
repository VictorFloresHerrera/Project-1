from abc import ABC, abstractmethod

from entities.employee import Employee


class EmployeeService(ABC):

    @abstractmethod
    def service_get_employee_by_id(self, userid: str) -> Employee:
        pass

    @abstractmethod
    def service_get_all_employee(self) -> list[Employee]:  # , employee: Employee
        pass

    @abstractmethod
    def service_update_employee(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def service_get_login_for_employee(self, employee: Employee) -> Employee:
        pass
