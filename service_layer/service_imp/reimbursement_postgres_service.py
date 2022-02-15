from custom_exceptions.caution_negative_number_exception import CautionNegativeNumberException
# from custom_exceptions.char_limit_exception import CharLimitException
from custom_exceptions.employee_nonexist_exception import EmployeeNonexistException
from custom_exceptions.invalid_acceptance_exception import InvalidAcceptanceException
from custom_exceptions.manager_nonexist_exception import ManagerNonexistException
from custom_exceptions.only_real_numbers_exception import OnlyRealNumbersException
#  from custom_exceptions.reimbursement_already_exist_exception import ReimbursementAlreadyExistException
#  from custom_exceptions.reimbursement_already_exist_exception import ReimbursementAlreadyExistException
from custom_exceptions.reimbursement_nonexist_exception import ReimbursementNonexistException
# from data_access_layer.abstract_classes.reimbursement_dao import ReimbursementDAO
# from data_access_layer.dao_imp.reimbursement_imp_dao import ReimbursementPostgresDAO
from data_access_layer.dao_imp.reimbursement_imp_dao import ReimbursementPostgresDAO
from entities.reimbursement import Reimbursement

from service_layer.abstract_classes.reimbursement_service import ReimbursementService


class ReimbursementPostgresService(ReimbursementService):  # ABC

    def __init__(self, reimbursement_dao: ReimbursementPostgresDAO):
        self.reimbursement_dao = reimbursement_dao

    def service_create_get_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        if reimbursement.acceptance == "Pending":
            if type(reimbursement.reimbursement) == int:
                if reimbursement.reimbursement > 0:
                    return self.reimbursement_dao.create_get_reimbursement(reimbursement)
                raise CautionNegativeNumberException("Cannot contain negative number.")
            raise OnlyRealNumbersException("Only real numbers allowed.")
        raise InvalidAcceptanceException("Invalid acceptance.")

    def service_select_get_reimbursement_id(self, reimbursement_id) -> Reimbursement:
        reimbursement_list = self.reimbursement_dao.select_get_all_reimbursement_information()
        for existing_reimbursement in reimbursement_list:
            if existing_reimbursement.reimbursement_id == reimbursement_id:
                return self.reimbursement_dao.select_get_reimbursement_id(reimbursement_id)
        raise ReimbursementNonexistException("Does not exist.")

    def service_select_get_all_reimbursement_information(self) -> list[Reimbursement]:
        return self.reimbursement_dao.select_get_all_reimbursement_information()

    def service_select_reimbursement_by_employee_id(self, employee_id) -> list[Reimbursement]:
        reimbursement_list = self.reimbursement_dao.select_get_all_reimbursement_information()
        for existing_reimbursement in reimbursement_list:
            if existing_reimbursement.employee_id == employee_id:
                return self.reimbursement_dao.select_reimbursement_by_employee_id(employee_id)
        raise EmployeeNonexistException("Does not exist.")

    def service_approve_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        reimbursement_list = self.reimbursement_dao.select_get_all_reimbursement_information()
        for existing_reimbursement in reimbursement_list:
            if existing_reimbursement.reimbursement_id == reimbursement.reimbursement_id:
                if existing_reimbursement.manager_id == reimbursement.manager_id:
                    if existing_reimbursement.employee_id == reimbursement.employee_id:
                        if reimbursement.acceptance == "Approve":
                            return self.reimbursement_dao.approve_reimbursement(reimbursement)
                        raise InvalidAcceptanceException("Invalid acceptance.")
                    raise EmployeeNonexistException("Does not exist.")
                raise ManagerNonexistException("Does not exist.")

    def service_deny_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        reimbursement_list = self.reimbursement_dao.select_get_all_reimbursement_information()
        for existing_reimbursement in reimbursement_list:
            if existing_reimbursement.reimbursement_id == reimbursement.reimbursement_id:
                if existing_reimbursement.manager_id == reimbursement.manager_id:
                    if existing_reimbursement.employee_id == reimbursement.employee_id:
                        if reimbursement.acceptance == "Denied":
                            return self.reimbursement_dao.deny_reimbursement(reimbursement)
                        raise InvalidAcceptanceException("Invalid acceptance.")
                    raise EmployeeNonexistException("Does not exist.")
                raise ManagerNonexistException("Does not exist.")

    def service_get_all_pending_reimbursement_by_manager_id(self, manager_id: int) -> list[Reimbursement]:
        reimbursement_list = self.reimbursement_dao.select_get_all_reimbursement_information()
        for existing_reimbursement in reimbursement_list:
            if existing_reimbursement.manager_id == manager_id:
                if existing_reimbursement.acceptance == "Pending":
                    return self.reimbursement_dao.get_all_pending_reimbursement_by_manager_id(manager_id)
        raise ManagerNonexistException("Does not exist.")

    def service_get_past_reimbursement_by_manager_id(self, manager_id: int) -> list[Reimbursement]:
        reimbursement_list = self.reimbursement_dao.select_get_all_reimbursement_information()
        for existing_reimbursement in reimbursement_list:
            if existing_reimbursement.manager_id == manager_id:
                if existing_reimbursement.acceptance != "Pending":
                    return self.reimbursement_dao.get_past_reimbursement_by_manager_id(manager_id)
        raise ManagerNonexistException("Does not exist.")

    def service_view_reimbursement_statistics(self, reimbursement: Reimbursement):
        pass

    def service_update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        result = self.reimbursement_dao.update_reimbursement(reimbursement)
        return result

    def get_number_of_reimbursement_requests_total(self):
        requests = self.reimbursement_dao.select_get_all_reimbursement_information()
        return len(requests)

    def get_number_of_reimbursement_requests_pending(self):
        requests = self.reimbursement_dao.select_get_all_reimbursement_information()
        pending = []
        for p in requests:
            if p.acceptance == "Pending":
                pending.append(p)
        return len(pending)

    def get_number_of_reimbursement_requests_approved(self):
        requests = self.reimbursement_dao.select_get_all_reimbursement_information()
        approved = []
        for a in requests:
            if a.acceptance == "Approve":
                approved.append(a)
        return len(approved)

    def get_number_of_reimbursement_requests_denied(self):
        requests = self.reimbursement_dao.select_get_all_reimbursement_information()
        denied = []
        for d in requests:
            if d.acceptance == "Denied":
                denied.append(d)
        return len(denied)

    def get_number_of_null_reimbursement_request(self):
        requests = self.reimbursement_dao.select_get_all_reimbursement_information()
        null = []
        for g in requests:
            if g.acceptance == "":
                null.append(g)
        return len(null)
