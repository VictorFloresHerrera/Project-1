from abc import abstractmethod, ABC

from entities.reimbursement import Reimbursement


class ReimbursementDAO(ABC):

    @abstractmethod
    def create_get_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def select_get_reimbursement_id(self, reimbursement_id) -> Reimbursement:
        pass

    @abstractmethod
    def select_get_all_reimbursement_information(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def select_reimbursement_by_employee_id(self, employee_id) -> list[Reimbursement]:
        pass

    @abstractmethod
    def approve_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def deny_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def get_all_pending_reimbursement_by_manager_id(self, manager_id) -> list[Reimbursement]:
        pass

    @abstractmethod
    def get_past_reimbursement_by_manager_id(self, manager_id) -> list[Reimbursement]:
        pass

