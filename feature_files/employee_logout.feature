Feature: Employee logout

  Scenario: As an employee I want to be able to logout to protect my information
    Given the Employee is already logged in
    When the employee clicks on the logout button
    Then the employee will return to the login page and have to log back in to view reimbursements