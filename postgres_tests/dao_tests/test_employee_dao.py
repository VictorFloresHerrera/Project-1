from entities.employee import Employee
from data_access_layer.dao_imp.employee_imp_dao import EmployeePostgresDAO

employee_dao = EmployeePostgresDAO()

update_employee: Employee = Employee(2, "4", "test", "e2", "test")
update_employee2: Employee = Employee(2, "4", "test", "e2", "test")


def test_get_login_for_employee_success():
    updated_employee = employee_dao.update_employee(update_employee)
    assert updated_employee

    # login_info = Employee(employee_id=3, first_name="Herrera", last_name="Herrera", user="e3", passcode="mycode3")
    # assert employee_dao.get_login_for_employee(login_info.user, login_info.passcode)


def test_get_employee_by_id():
    login_info = Employee(employee_id=1, first_name="Vic", last_name="Vic", user="test", passcode="mycode")
    assert employee_dao.get_employee_info(login_info.employee_id)


def test_get_all_employee():
    employee_list = employee_dao.get_all_employees()
    return employee_list


def test_update_employee():
    updated_employee = employee_dao.update_employee(update_employee)
    assert updated_employee
