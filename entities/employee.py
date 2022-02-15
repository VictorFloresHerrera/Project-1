class Employee:
    def __init__(self, employee_id: int = 0, first_name: str = 'first', last_name: str = 'last',
                 userid: str = 'userid', passcode: str = 'passcode'):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.userid = userid
        self.passcode = passcode

    def make_employee_dictionary(self):
        return {
            "employeeId": self.employee_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "userid": self.userid,
            "passcode": self.passcode
        }

    def __str__(self):
        return "employee Id: {}, first name: {}, last name: {},userid: " \
               "{}, passcode: {}".format(self.employee_id,
                                         self.first_name,
                                         self.last_name,
                                         self.userid,
                                         self.passcode)
