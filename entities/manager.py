class Manager:

    def __init__(self, manager_id: int = 0, first_name: str = 'first', last_name: str = 'last', userid: str = 'userid', passcode: str = 'passcode'):
        self.manager_id = manager_id
        self.first_name = first_name
        self.last_name = last_name
        self.userid = userid
        self.passcode = passcode

    def make_manager_dictionary(self):
        return {
            "managerId": self.manager_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "userid": self.userid,
            "passcode": self.passcode,

        }

    def __str__(self):
        return " manager Id: {}, first Name: {}, last Name: {}, userid: {}, passcode: {} ".format \
            (self.manager_id, self.first_name, self.last_name, self.userid, self.passcode)
