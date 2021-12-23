class EmployeeNonexistException(Exception):
    def __init__(self, message: str):
        self.message = message
