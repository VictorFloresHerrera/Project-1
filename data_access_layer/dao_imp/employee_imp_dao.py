from typing import List

from data_access_layer.abstract_classes.employee_dao import EmployeeDAO
from entities.employee import Employee
from util.database_connection import connection
import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")


class EmployeePostgresDAO(EmployeeDAO):

    def get_employee_info(self, employee_id) -> Employee:
        sql = "select * from employee where employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        employee_record = cursor.fetchone()
        employee = Employee(*employee_record)
        return employee

    def get_all_employees(self) -> List[Employee]:
        sql = "select * from employee"
        cursor = connection.cursor()
        cursor.execute(sql)
        account_record = cursor.fetchall()
        employees_list = []
        for employee in account_record:
            employees_list.append(Employee(*employee))
        return employees_list

    def update_employee(self, employee: Employee) -> Employee:
        sql = "update employee set first_name = %s, last_name = %s, passcode = %s where employee_id " \
              "= %s "
        cursor = connection.cursor()
        cursor.execute(sql, (
            employee.first_name, employee.last_name, employee.passcode, employee.employee_id))
        connection.commit()
        return employee

    def get_login_for_employee(self, user: str, passcode: str) -> Employee:
        sql = 'select * from employee where user = %s and passcode = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (user, passcode))
        employee_record = cursor.fetchone()
        print(employee_record)
        this_employee = Employee(*employee_record)
        logging.debug(this_employee)
        return this_employee
