Feature: Manager deny a reimbursement.

  Scenario: as a manager, I should be to deny reimbursement requests and leave comment because they are legitimate
    Given The managers is in the manager page
    When the managers enter the reimbursement id in the reimbursement id input box
    When the managers enter the employee id in the employee id input box
    When the managers enter the manager id in the manager id input box
    When the managers enter the reimbursement amount in the reimbursement amount input box
    When the managers enter the reason in the reason input box
    When the managers enter the approval in the approval input box
    When the managers enter the manager comment in the manager comment input box
    When the manager clicks the deny button
    Then one reimbursement is deny and sent to the previous reimbursements