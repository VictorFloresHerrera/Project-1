from abc import abstractmethod, ABC

from entities.reimbursement import Reimbursement


class ReimbursementService(ABC):

    @abstractmethod
    def service_create_get_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def service_select_get_reimbursement_id(self, reimbursement_id) -> Reimbursement:
        pass

    @abstractmethod
    def service_select_get_all_reimbursement_information(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_select_reimbursement_by_employee_id(self, employee_id) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_approve_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def service_deny_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def service_update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def service_get_all_pending_reimbursement_by_manager_id(self, manager_id: int) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_get_past_reimbursement_by_manager_id(self, manager_id: int) -> list[Reimbursement]:
        pass

    @abstractmethod
    def get_number_of_reimbursement_requests_total(self):
        pass

    @abstractmethod
    def get_number_of_reimbursement_requests_pending(self):
        pass

    @abstractmethod
    def get_number_of_reimbursement_requests_approved(self):
        pass

    @abstractmethod
    def get_number_of_reimbursement_requests_denied(self):
        pass

    @abstractmethod
    def get_number_of_null_reimbursement_request(self):
        pass


