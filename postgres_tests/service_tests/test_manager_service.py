from custom_exceptions.login_failed_exception import LoginFailedException
from entities.manager import Manager
from data_access_layer.dao_imp.manager_imp_dao import ManagerPostgresDAO
from service_layer.service_imp.manager_postgres_service import ManagerPostgresService

manager_dao = ManagerPostgresDAO()
manager_service = ManagerPostgresService(manager_dao)

# manager_with_wrong_login = Manager("Vic", "Vic", 1, "my")


def test_service_get_login_for_manager():
    try:
        manager_service.service_get_login_for_manager("2", "my")
        assert False
    except LoginFailedException as e:
        assert str(e) == "Login Failed."
