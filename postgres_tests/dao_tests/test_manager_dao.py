from entities.manager import Manager
from data_access_layer.dao_imp.manager_imp_dao import ManagerPostgresDAO

manager_dao = ManagerPostgresDAO()


update_manager: Manager = Manager(2, "4", "test", "e2",  "test")


def test_get_login_for_manager_success():
    updated_manager = manager_dao.update_manager(update_manager)
    assert updated_manager
    # login_info = Manager(manager_id=1, first_name="Vic", last_name="Vic", user="m1", passcode="mycode1")
    # assert manager_dao.get_login_for_manager(login_info.user, login_info.passcode)


def test_get_manager_by_id():
    login_info = Manager(manager_id=1, first_name="Vic", last_name="Vic", user="test", passcode="mycode")
    assert manager_dao.get_manager_info(login_info.manager_id)


def test_get_all_managers():
    manager_list = manager_dao.get_all_managers()
    return manager_list


def test_update_manager():
    updated_manager = manager_dao.update_manager(update_manager)
    assert updated_manager
