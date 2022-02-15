Feature: Submit a reimbursement
  
  Scenario: As an employee I want to submit a reimbursement to get money back.
    Given the employee is on the employee page
    When the employee enters the employee id in the employee id  input box
    When the employee enters the manager id in the manager id  input box
    When the employee enters the reimbursement amount in the reimbursement amount  input box
    When the employee enters the reason in the reason  input box
    When the employee clicks the submit button
    Then a new reimbursement is added to the Reimbursement Information