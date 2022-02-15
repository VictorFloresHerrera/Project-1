Feature: Employee Login

  Scenario: As an employee I want to login so I can manage my reimbursements
    Given The employee is on login page
    When The employee enters their userid in the userid input box
    When The employee enters their passcode in the passcode input box
    When The employee clicks on the Login button
    Then The employee should be logged in and redirected to the employee home page