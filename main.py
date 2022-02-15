from flask import Flask, request, jsonify
import logging
from flask_cors import CORS
from custom_exceptions.caution_negative_number_exception import CautionNegativeNumberException
from custom_exceptions.employee_id_nonexist_exception import EmployeeIdNonexistException
# from custom_exceptions.employee_nonexist_exception import EmployeeNonexistException
from custom_exceptions.employee_nonexist_exception import EmployeeNonexistException
from custom_exceptions.invalid_acceptance_exception import InvalidAcceptanceException
from custom_exceptions.login_failed_exception import LoginFailedException
from custom_exceptions.manager_nonexist_exception import ManagerNonexistException
from custom_exceptions.manager_user_not_found_exception import ManagerUserNotFoundException
from custom_exceptions.reimbursement_duplicate_exception import ReimbursementDuplicateException
from data_access_layer.dao_imp.manager_imp_dao import ManagerPostgresDAO
# from data_access_layer.dao_imp.reimbursement_imp_dao import ReimbursementPostgresDAO
from data_access_layer.dao_imp.reimbursement_imp_dao import ReimbursementPostgresDAO
from entities.employee import Employee
from entities.manager import Manager
from data_access_layer.dao_imp.employee_imp_dao import EmployeePostgresDAO
from entities.reimbursement import Reimbursement
# from postgres_tests.service_tests.test_reimbursement_service import reimbursement_service
from service_layer.service_imp.employee_postgres_service import EmployeePostgresService
from service_layer.service_imp.manager_postgres_service import ManagerPostgresService
from service_layer.service_imp.reimbursement_postgres_service import ReimbursementPostgresService

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)
CORS(app)

employee_dao = EmployeePostgresDAO()
employee_service = EmployeePostgresService(employee_dao)

manager_dao = ManagerPostgresDAO()
manager_service = ManagerPostgresService(manager_dao)

reimbursement_dao = ReimbursementPostgresDAO()
reimbursement_service = ReimbursementPostgresService(reimbursement_dao)


@app.get("/employee/<userid>")
def get_employee_by_id(userid: str):
    try:
        result = employee_service.service_get_employee_by_id(userid)
        result_as_dictionary = result.make_employee_dictionary()
        result_as_json = jsonify(result_as_dictionary)
        return result_as_json
    except EmployeeIdNonexistException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get("/employee")
def get_all_employees():
    employees = employee_service.service_get_all_employee()
    employees_as_dictionary = []
    for employee in employees:
        dictionary_employee = employee.make_employee_dictionary()
        employees_as_dictionary.append(dictionary_employee)
    return jsonify(employees_as_dictionary), 200


@app.post("/employee/login")
def service_get_login_for_employee():
    result = request.get_json()
    this_id = result["userid"]
    this_passcode = result["passcode"]

    try:
        employee_returning = Employee(userid=this_id, passcode=this_passcode)
        employee_object = employee_service.service_get_login_for_employee(employee_returning)
        employee_dict = employee_object.make_employee_dictionary()
        employee_json = jsonify(employee_dict)
        return employee_json
    except LoginFailedException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


#######################################################################################
# result = request.get_json()
# if result:
#     #  objects for postman
#     user = result["user"]
#     employee_passcode = result["passcode"]
#     try:
#         #  Returning the objects
#         return_employee: Employee = employee_service.service_get_login_for_employee()
#         #  Placing objects method into object
#         # employee_object = employee_service.service_get_login_for_employee(return_employee)
#         #  Creating dictionary
#         employee_dictionary = return_employee.make_employee_dictionary()
#         #  Returning dictionary into JSON
#         employee_json = jsonify(employee_dictionary)
#         return employee_json
#         #  Raising Exception
#     except LoginFailedException as e:
#         exception_dictionary = {"message": str(e)}
#         exception_json = jsonify(exception_dictionary)
#         return exception_json


@app.get("/employee/reimbursement/<employee_id>")
def get_employee_reimbursement_by_employee_id(employee_id: int):
    reimbursement_as_reimbursement = reimbursement_service.service_select_reimbursement_by_employee_id(int(employee_id))
    reimbursement_as_dictionary = []
    for reimbursements in reimbursement_as_reimbursement:
        dictionary_reimbursement = reimbursements.make_reimbursement_dictionary()
        reimbursement_as_dictionary.append(dictionary_reimbursement)
    return jsonify(reimbursement_as_dictionary)


@app.post("/reimbursement")
def service_create_reimbursement():
    try:
        result = request.get_json()
        new_reimbursement = Reimbursement(
            result["reimbursementId"],
            result["employeeId"],
            result["managerId"],
            int(result["reimbursement"]),
            result["reasonwhy"],
            result["acceptance"],
            result["managerComment"]
        )
        reimbursement_to_return = reimbursement_service.service_create_get_reimbursement(new_reimbursement)
        reimbursement_as_dictionary = reimbursement_to_return.make_reimbursement_dictionary()
        reimbursement_as_json = jsonify(reimbursement_as_dictionary)
        return reimbursement_as_json
    except ReimbursementDuplicateException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except CautionNegativeNumberException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get("/reimbursement/all")
def get_all_reimbursement_information():
    reimbursement_as_reimbursement = reimbursement_service.service_select_get_all_reimbursement_information()
    reimbursement_as_dictionary = []
    for reimbursements in reimbursement_as_reimbursement:
        dictionary_reimbursement = reimbursements.make_reimbursement_dictionary()
        reimbursement_as_dictionary.append(dictionary_reimbursement)
    return jsonify(reimbursement_as_dictionary)


@app.get("/past/reimbursements/<manager_id>")
def get_all_past_reimbursement_information(manager_id: int):
    reimbursement_as_reimbursement = reimbursement_service.service_get_past_reimbursement_by_manager_id(
        int(manager_id))
    reimbursement_as_dictionary = []
    for reimbursements in reimbursement_as_reimbursement:
        dictionary_reimbursement = reimbursements.make_reimbursement_dictionary()
        reimbursement_as_dictionary.append(dictionary_reimbursement)
    return jsonify(reimbursement_as_dictionary)


@app.get("/manager/pending/reimbursement/<manager_id>")
def get_all_pending_reimbursement_by_manager_id(manager_id: int):
    reimbursement_as_reimbursement = reimbursement_service.service_get_all_pending_reimbursement_by_manager_id(
        int(manager_id))
    reimbursement_as_dictionary = []
    for reimbursements in reimbursement_as_reimbursement:
        dictionary_reimbursement = reimbursements.make_reimbursement_dictionary()
        reimbursement_as_dictionary.append(dictionary_reimbursement)
    return jsonify(reimbursement_as_dictionary)


##################################################################################################################


@app.get("/manager/<userid>")
def get_manager_by_id(userid: str):
    try:
        result = manager_service.service_get_manager_by_id(userid)
        result_as_dictionary = result.make_manager_dictionary()
        result_as_json = jsonify(result_as_dictionary)
        return result_as_json
    except ManagerUserNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get("/manager/null/<userid>")
def get_manager_by_id_null(userid: str):
    try:
        result = manager_service.service_get_manager_by_id(userid)
        result_as_dictionary = result.make_manager_dictionary()
        result_as_json = jsonify(result_as_dictionary)
        return result_as_json
    except ManagerUserNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get("/manager")
def get_all_managers():
    managers = manager_service.service_get_all_managers()
    managers_as_dictionary = []
    for manager in managers:
        dictionary_manager = manager.make_manager_dictionary()
        managers_as_dictionary.append(dictionary_manager)
    return jsonify(managers_as_dictionary), 200


@app.post("/manager/login")
def service_get_login_for_manager():
    result = request.get_json()
    if result:
        #  objects for postman
        userid = result["userid"]
        manager_passcode = result["passcode"]
        try:
            #  Returning the objects
            return_manager: Manager = manager_service.service_get_login_for_manager(userid, manager_passcode)
            #  Placing objects method into object
            # manager_object = manager_service.service_get_login_for_manager(return_manager)
            #  Creating dictionary
            manager_dictionary = return_manager.make_manager_dictionary()
            #  Returning dictionary into JSON
            manager_json = jsonify(manager_dictionary)
            return manager_json
            #  Raising Exception
        except LoginFailedException as e:
            exception_dictionary = {"message": str(e)}
            exception_json = jsonify(exception_dictionary)
            return exception_json


################################################################################################################

@app.patch("/reimbursement/approve/<reimbursement_id>")
def service_approve_reimbursement(reimbursement_id):
    try:
        result = request.get_json()
        new_reimbursement = Reimbursement(
            int(reimbursement_id),
            int(result["employeeId"]),
            int(result["managerId"]),
            result["reimbursement"],
            result["reasonwhy"],
            result["acceptance"],
            result["managerComment"]
        )
        reimbursement_to_return = reimbursement_service.service_approve_reimbursement(new_reimbursement)
        return "Manager has updated your reimbursement information" + str(reimbursement_to_return)
    except InvalidAcceptanceException as e:
        return str(e)
    except EmployeeNonexistException as e:
        return str(e)
    except ManagerNonexistException as e:
        return str(e)


@app.patch("/reimbursement/deny/<reimbursement_id>")
def service_deny_reimbursement(reimbursement_id):
    try:
        result = request.get_json()
        new_reimbursement = Reimbursement(
            int(reimbursement_id),
            int(result["employeeId"]),
            int(result["managerId"]),
            result["reimbursement"],
            result["reasonwhy"],
            result["acceptance"],
            result["managerComment"]
        )
        reimbursement_to_return = reimbursement_service.service_deny_reimbursement(new_reimbursement)
        return "Manager has updated your reimbursement information" + str(reimbursement_to_return)
    except InvalidAcceptanceException as e:
        return str(e)
    except EmployeeNonexistException as e:
        return str(e)
    except ManagerNonexistException as e:
        return str(e)


app.run()
