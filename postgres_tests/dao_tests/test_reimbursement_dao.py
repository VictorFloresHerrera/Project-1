from data_access_layer.dao_imp.reimbursement_imp_dao import ReimbursementPostgresDAO
from entities.reimbursement import Reimbursement

reimbursement_dao = ReimbursementPostgresDAO()


# def test_create_reimbursement_success():
#     login_info = Reimbursement(reimbursement_id=1, employee_id=1, manager_id=1, reimbursement=1, reasonwhy="idk",
#                                acceptance="idk", manager_comment="dik")
#     assert reimbursement_dao.create_get_reimbursement(login_info)


def test_get_reimbursement_by_id_success():
    show = reimbursement_dao.select_get_reimbursement_id(3)
    assert show.reimbursement_id == 3


def test_get_all_reimbursement_success():
    list_example = reimbursement_dao.select_get_all_reimbursement_information()
    return len(list_example) >= 2


def test_get_all_reimbursement_by_employee_id_success():
    employee_reimbursement_list = reimbursement_dao.select_reimbursement_by_employee_id(1)
    assert len(employee_reimbursement_list) >= 1


def test_deny_reimbursements_by_id_success():
    denied_reimbursement = Reimbursement(reimbursement_id=1, employee_id=1, manager_id=1, reimbursement=1,
                                         reasonwhy="idk",
                                         acceptance="accept", manager_comment="dik")
    assert reimbursement_dao.deny_reimbursement(denied_reimbursement)


def test_accept_reimbursements_by_id_success():
    accept_reimbursement = Reimbursement(reimbursement_id=1, employee_id=1, manager_id=1, reimbursement=1,
                                         reasonwhy="idk",
                                         acceptance="accept", manager_comment="dik")
    assert reimbursement_dao.approve_reimbursement(accept_reimbursement)


def test_update_reimbursement_success():
    updated_reimbursement = Reimbursement(reimbursement_id=1, employee_id=50, manager_id=50, reimbursement=50,
                                          reasonwhy="test",
                                          acceptance="test", manager_comment="test")
    assert reimbursement_dao.update_reimbursement(updated_reimbursement)


