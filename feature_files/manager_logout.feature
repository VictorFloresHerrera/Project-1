Feature: Logout

    Scenario: as a manager, I should be able to logout so my information does not remain available on my computer
    Given the manager is on the manager page
    When the manager clicks the logout button
    Then the manager is on the login page