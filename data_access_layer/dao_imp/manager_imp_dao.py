from typing import List

# from custom_exceptions.login_failed_exception import LoginFailedException
from custom_exceptions.login_failed_exception import LoginFailedException
from data_access_layer.abstract_classes.manager_dao import ManagerDAO
# from entities import manager
from entities.manager import Manager
from util.database_connection import connection
import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")


class ManagerPostgresDAO(ManagerDAO):

    def get_manager_info(self, manager_id) -> Manager:
        sql = "select * from manager where manager_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [manager_id])
        manager_record = cursor.fetchone()
        manager = Manager(*manager_record)
        return manager

    def get_all_managers(self) -> List[Manager]:
        sql = "select * from manager"
        cursor = connection.cursor()
        cursor.execute(sql)
        account_record = cursor.fetchall()
        managers_list = []
        for manager in account_record:
            managers_list.append(Manager(*manager))
        return managers_list

    def update_manager(self, manager: Manager) -> Manager:
        sql = "update manager set first_name = %s, last_name = %s, passcode = %s where manager_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (manager.first_name, manager.last_name, manager.passcode, manager.manager_id))
        connection.commit()
        return manager

    def get_login_for_manager(self, user: str, passcode: str) -> Manager:
        sql = "select * from manager where user= %s and passcode = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (user, passcode))
        manager_record = cursor.fetchone()
        this_manager = Manager(*manager_record)
        logging.debug(this_manager)
        return this_manager


