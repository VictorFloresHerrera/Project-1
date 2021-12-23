from custom_exceptions.login_failed_exception import LoginFailedException
from custom_exceptions.manager_user_not_found_exception import ManagerUserNotFoundException
from data_access_layer.abstract_classes.manager_dao import ManagerDAO
from data_access_layer.dao_imp.manager_imp_dao import ManagerPostgresDAO
from entities.manager import Manager
from service_layer.abstract_classes.manager_service import ManagerService


class ManagerPostgresService(ManagerService):

    def __init__(self, manager_dao: ManagerPostgresDAO):
        self.manager_dao = manager_dao

    def service_get_manager_info(self, user: str) -> Manager:
        manager_list = self.manager_dao.get_all_managers()
        for existing_manager in manager_list:
            if existing_manager.user == user:
                return self.manager_dao.get_manager_info(user)
        raise ManagerUserNotFoundException("Manager username was not found")

    def service_get_all_managers(self) -> list[Manager]:
        all_manager = self.manager_dao.get_all_managers()
        return all_manager

    def service_update_manager(self, manager: Manager) -> Manager:
        updated_manager = self.service_update_manager(manager)
        return updated_manager

    def service_get_login_for_manager(self, user: str, passcode: str) -> Manager:
        manager_list = self.manager_dao.get_all_managers()
        for existing_manager in manager_list:
            if existing_manager.user == user and existing_manager.passcode == passcode:
                return self.manager_dao.get_login_for_manager(user, passcode)
        raise LoginFailedException("Login Failed.")


