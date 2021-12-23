class Reimbursement:
    def __init__(self, reimbursement_id: int, employee_id: int, manager_id: int,
                 reimbursement: int, reasonwhy: str, acceptance: str, manager_comment: str):
        self.reimbursement_id = reimbursement_id
        self.employee_id = employee_id
        self.manager_id = manager_id
        self.reimbursement = reimbursement
        self.reasonwhy = reasonwhy
        self.acceptance = acceptance
        self.manager_comment = manager_comment

    def make_reimbursement_dictionary(self):
        return {
            "reimbursementId": self.reimbursement_id,
            "employeeId": self.employee_id,
            "managerId": self.manager_id,
            "reimbursement": self.reimbursement,
            "reasonwhy": self.reasonwhy,
            "acceptance": self.acceptance,
            "managerComment": self.manager_comment
        }

    def __str__(self):
        return "reimbursement id: {}, employee id: {}, manager id: {}, reimbursement: {}, reasonwhy:{}, acceptance: {}, " \
               "manager comment: {}".format(self.reimbursement_id, self.employee_id, self.manager_id,
                                            self.reimbursement, self.reasonwhy, self.acceptance, self.manager_comment)
