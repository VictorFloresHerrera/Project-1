from abc import ABC, abstractmethod

from entities.manager import Manager


class ManagerDAO(ABC):

    @abstractmethod
    def get_manager_by_id(self, userid) -> Manager:
        pass

    @abstractmethod
    def get_all_managers(self) -> list[Manager]:
        pass

    @abstractmethod
    def update_manager(self, manager: Manager) -> Manager:
        pass

    @abstractmethod
    def get_login_for_manager(self, userid: str, passcode: str):
        pass

