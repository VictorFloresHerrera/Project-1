from data_access_layer.abstract_classes.reimbursement_dao import ReimbursementDAO
from entities.reimbursement import Reimbursement
from util.database_connection import connection


class ReimbursementPostgresDAO(ReimbursementDAO):

    def create_get_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = "insert into reimbursement values(default, %s, %s, %s, %s, %s, %s) returning reimbursement_id"
        cursor = connection.cursor()
        cursor.execute(sql, (
            reimbursement.employee_id, reimbursement.manager_id, reimbursement.reimbursement, reimbursement.reasonwhy,
            reimbursement.acceptance, reimbursement.manager_comment))
        connection.commit()
        reimbursement_id = cursor.fetchone()[0]
        reimbursement.reimbursement_id = reimbursement_id
        return reimbursement

    def select_get_reimbursement_id(self, reimbursement_id) -> Reimbursement:
        sql = "select * from reimbursement where reimbursement_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        reimbursement_record = cursor.fetchone()
        reimbursement = Reimbursement(*reimbursement_record)
        return reimbursement

    def select_get_all_reimbursement_information(self) -> list[Reimbursement]:
        sql = "select * from reimbursement"
        cursor = connection.cursor()
        cursor.execute(sql)
        reimbursement_records = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in reimbursement_records:
            reimbursement_list.append(Reimbursement(*reimbursement))
        return reimbursement_list

    def select_reimbursement_by_employee_id(self, employee_id) -> list[Reimbursement]:
        sql = "select * from reimbursement where employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        reimbursement_record = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in reimbursement_record:
            reimbursement_list.append(Reimbursement(*reimbursement))
        return reimbursement_list

    def approve_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = "update reimbursement set acceptance = %s, manager_comment = %s where reimbursement_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement.acceptance, reimbursement.manager_comment, reimbursement.reimbursement_id])
        connection.commit()
        return reimbursement

    def deny_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = "update reimbursement set acceptance = %s, manager_comment = %s where reimbursement_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement.acceptance, reimbursement.manager_comment, reimbursement.reimbursement_id])
        connection.commit()
        return reimbursement

    def update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = "update reimbursement set employee_id = %s, manager_id = %s, reimbursement = %s, reasonwhy = %s, " \
              "acceptance = %s, manager_comment = %s where reimbursement_id = %s "
        cursor = connection.cursor()
        cursor.execute(sql, (
            reimbursement.employee_id, reimbursement.manager_id, reimbursement.reimbursement,
            reimbursement.reasonwhy, reimbursement.acceptance, reimbursement.manager_comment,
            reimbursement.reimbursement_id))
        connection.commit()
        return reimbursement

    def get_past_reimbursement_by_manager_id(self, manager_id) -> list[Reimbursement]:
        sql = """select * from reimbursement where manager_id = %s and acceptance <> 'Pending'"""
        cursor = connection.cursor()
        cursor.execute(sql, [manager_id])
        past_reimbursements_records = cursor.fetchall()
        past_reimbursements_list = []
        for past_reimbursement in past_reimbursements_records:
            past_reimbursements_list.append(Reimbursement(*past_reimbursement))
        return past_reimbursements_list

    def get_all_pending_reimbursement_by_manager_id(self, manager_id) -> list[Reimbursement]:
        sql = """select * from reimbursement where manager_id = %s and acceptance = 'Pending'"""
        cursor = connection.cursor()
        cursor.execute(sql, [manager_id])
        pending_reimbursement_records = cursor.fetchall()
        pending_reimbursement_list = []
        for pending_reimbursement in pending_reimbursement_records:
            pending_reimbursement_list.append(Reimbursement(*pending_reimbursement))
        return pending_reimbursement_list
