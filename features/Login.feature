Feature: Test Login
  Scenario: Test Login Q
    Given Login Page should open
    When Enter username "democlientuat@gmail.com" and password "Kanaka@123"
    Then Click on Login
    Then User should logeed in successfully
