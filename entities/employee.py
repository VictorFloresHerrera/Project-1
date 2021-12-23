class Employee:
    def __init__(self, employee_id: int, first_name: str, last_name: str, user: str, passcode: str):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.user = user
        self.passcode = passcode

    def make_employee_dictionary(self):
        return {
            "employeeId": self.employee_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "user": self.user,
            "passcode": self.passcode
        }

    def __str__(self):
        return "employee Id: {}, first name: {}, last name: {},user: " \
               "{}, passcode: {}".format(self.employee_id,
                                         self.first_name,
                                         self.last_name,
                                         self.user,
                                         self.passcode)
