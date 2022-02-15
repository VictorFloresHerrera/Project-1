from custom_exceptions.login_failed_exception import LoginFailedException
from entities.employee import Employee
from data_access_layer.dao_imp.employee_imp_dao import EmployeePostgresDAO
from service_layer.service_imp.employee_postgres_service import EmployeePostgresService

employee_dao = EmployeePostgresDAO()
employee_service = EmployeePostgresService(employee_dao)

employee_with_wrong_login = Employee(1, "Victor", "Victor", "1", "my")


def test_service_get_login_for_employee():
    try:
        employee_service.service_get_login_for_employee(employee_with_wrong_login)
        assert False
    except LoginFailedException as e:
        assert str(e) == "Login Failed."
