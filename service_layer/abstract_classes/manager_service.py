from abc import ABC, abstractmethod

from entities.manager import Manager


class ManagerService(ABC):

    @abstractmethod
    def service_get_manager_by_id(self, userid: str) -> Manager:
        pass

    @abstractmethod
    def service_get_all_managers(self) -> list[Manager]:  # , manager: Manager
        pass

    @abstractmethod
    def service_update_manager(self, manager: Manager) -> Manager:
        pass

    @abstractmethod
    def service_get_login_for_manager(self, userid: str, passcode: str):
        pass

