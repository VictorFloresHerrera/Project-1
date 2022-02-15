Feature: Manager approve a reimbursement.

  Scenario: as a manager, I should be to approve reimbursement requests and leave comment because they are legitimate
    Given The manager is in the manager page
    When the manager enter the reimbursement id in the reimbursement id input box
    When the manager enter the employee id in the employee id input box
    When the manager enter the manager id in the manager id input box
    When the manager enter the reimbursement amount in the reimbursement amount input box
    When the manager enter the reason in the reason input box
    When the manager enter the approval in the approval input box
    When the manager enter the manager comment in the manager comment input box
    When the manager clicks the approve button
    Then one reimbursement is approved and sent to the previous reimbursements