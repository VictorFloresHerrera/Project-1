from custom_exceptions.caution_negative_number_exception import CautionNegativeNumberException
from custom_exceptions.employee_nonexist_exception import EmployeeNonexistException
#  from custom_exceptions.reimbursement_already_exist_exception import ReimbursementAlreadyExistException
from custom_exceptions.invalid_acceptance_exception import InvalidAcceptanceException
from custom_exceptions.manager_nonexist_exception import ManagerNonexistException
from custom_exceptions.only_real_numbers_exception import OnlyRealNumbersException
from custom_exceptions.reimbursement_nonexist_exception import ReimbursementNonexistException
from data_access_layer.dao_imp.reimbursement_imp_dao import ReimbursementPostgresDAO
from entities.reimbursement import Reimbursement
from service_layer.abstract_classes.reimbursement_service import ReimbursementService
from service_layer.service_imp.reimbursement_postgres_service import ReimbursementPostgresService

reimbursement_dao = ReimbursementPostgresDAO()
reimbursement_service = ReimbursementPostgresService(reimbursement_dao)

create_reimbursement_sad_test = Reimbursement(1, 2, 3, -4, "test", "Pending", "")  # Negative number
create_reimbursement_sad_test2 = Reimbursement(1, 2, 3, 20.22, "test", "Pending", "")  # Only real Number
create_reimbursement_sad_test3 = Reimbursement(1, 2, 3, 4, "test", "P", "")  # Invalid Acceptance
approve_or_deny_reimbursement_sad_test = Reimbursement(4, 1, 1, 500, "test", "test", "")  # Acceptance
approve_or_deny_reimbursement_sad_test2 = Reimbursement(4, 1, 2, 5, "test", "test", "")  # Manager
approve_or_deny_reimbursement_sad_test3 = Reimbursement(4, 30, 1, 50, "test", "test", "")  # Employee


def test_service_create_get_reimbursement():
    try:
        reimbursement_service.service_create_get_reimbursement(create_reimbursement_sad_test)
        assert False
    except CautionNegativeNumberException as e:
        assert str(e) == "Cannot contain negative number."


def test_service_create_get_reimbursement2():
    try:
        reimbursement_service.service_create_get_reimbursement(create_reimbursement_sad_test2)
        assert False
    except OnlyRealNumbersException as e:
        assert str(e) == "Only real numbers allowed."


def test_service_create_get_reimbursement3():
    try:
        reimbursement_service.service_create_get_reimbursement(create_reimbursement_sad_test3)
        assert False
    except InvalidAcceptanceException as e:
        assert str(e) == "Invalid acceptance."


def test_get_reimbursement_by_id_fail():
    try:
        reimbursement_service.service_select_get_reimbursement_id(2000)
        assert False
    except ReimbursementNonexistException as e:
        assert str(e) == "Does not exist."


def test_get_all_reimbursements_by_employee_id_fail():
    try:
        reimbursement_service.service_select_reimbursement_by_employee_id(3000)
        assert False
    except EmployeeNonexistException as e:
        assert str(e) == "Does not exist."


def test_approve_reimbursement_fail_by_approval():
    try:
        reimbursement_service.service_approve_reimbursement(approve_or_deny_reimbursement_sad_test)
        assert False
    except InvalidAcceptanceException as e:
        assert str(e) == "Invalid acceptance."


def test_approve_reimbursement_fail_by_manager_id():
    try:
        reimbursement_service.service_approve_reimbursement(approve_or_deny_reimbursement_sad_test2)
        assert False
    except ManagerNonexistException as e:
        assert str(e) == "Does not exist."


def test_approve_reimbursement_fail_by_employee_id():
    try:
        reimbursement_service.service_approve_reimbursement(approve_or_deny_reimbursement_sad_test3)
        assert False
    except EmployeeNonexistException as e:
        assert str(e) == "Does not exist."


def test_deny_reimbursement_fail_by_approval():
    try:
        reimbursement_service.service_deny_reimbursement(approve_or_deny_reimbursement_sad_test)
        assert False
    except InvalidAcceptanceException as e:
        assert str(e) == "Invalid acceptance."


def test_deny_reimbursement_fail_by_manager_id():
    try:
        reimbursement_service.service_deny_reimbursement(approve_or_deny_reimbursement_sad_test2)
        assert False
    except ManagerNonexistException as e:
        assert str(e) == "Does not exist."


def test_deny_reimbursement_fail_by_employee_id():
    try:
        reimbursement_service.service_deny_reimbursement(approve_or_deny_reimbursement_sad_test3)
        assert False
    except EmployeeNonexistException as e:
        assert str(e) == "Does not exist."


def test_get_all_pending_fail_by_manager_id():
    try:
        reimbursement_service.service_get_all_pending_reimbursement_by_manager_id(2000)
        assert False
    except ManagerNonexistException as e:
        assert str(e) == "Does not exist."


def test_get_all_past_fail_by_manager_id():
    try:
        reimbursement_service.service_get_past_reimbursement_by_manager_id(3000)
        assert False
    except ManagerNonexistException as e:
        assert str(e) == "Does not exist."
