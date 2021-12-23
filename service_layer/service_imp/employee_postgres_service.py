from custom_exceptions.employee_user_not_found_exception import EmployeeUserNotFound
from custom_exceptions.login_failed_exception import LoginFailedException
# from data_access_layer.abstract_classes.employee_dao import EmployeeDAO
from data_access_layer.dao_imp.employee_imp_dao import EmployeePostgresDAO
from entities.employee import Employee
from service_layer.abstract_classes.employee_service import EmployeeService


class EmployeePostgresService(EmployeeService):

    def __init__(self, employee_dao: EmployeePostgresDAO):
        self.employee_dao = employee_dao

    def service_get_employee_info(self, user: str) -> Employee:
        employee_list = self.employee_dao.get_all_employees()
        for existing_employee in employee_list:
            if existing_employee.user == user:
                return self.employee_dao.get_employee_info(user)
        raise EmployeeUserNotFound("Employee username was not found")

    def service_get_all_employee(self) -> list[Employee]:
        all_employee = self.employee_dao.get_all_employees()
        return all_employee

    def service_update_employee(self, employee: Employee) -> Employee:
        updated_employee = self.service_update_employee(employee)
        return updated_employee

    def service_get_login_for_employee(self, user: str, passcode: str) -> Employee:
        employee_list = self.employee_dao.get_all_employees()
        for existing_employee in employee_list:
            if existing_employee.user == user and existing_employee.passcode == passcode:
                return self.employee_dao.get_login_for_employee(user, passcode)
        raise LoginFailedException("Login Failed.")


