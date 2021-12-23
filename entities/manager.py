class Manager:

    def __init__(self, manager_id: int, first_name: str, last_name: str, user: str, passcode: str):
        self.manager_id = manager_id
        self.first_name = first_name
        self.last_name = last_name
        self.user = user
        self.passcode = passcode

    def make_manager_dictionary(self):
        return {
            "managerId": self.manager_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "user": self.user,
            "passcode": self.passcode,

        }

    def __str__(self):
        return " manager Id: {}, first Name: {}, last Name: {}, user: {}, passcode: {} ".format \
            (self.manager_id, self.first_name, self.last_name, self.user, self.passcode)
