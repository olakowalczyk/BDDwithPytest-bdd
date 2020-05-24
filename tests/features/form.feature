Feature: Registration form
  As a web user,
  I want to register new user.

  Background:
      Given the form page is displayed

  Scenario Outline: Register a new user
      When new "<firstname>" is entered to the form
      And new "<lastname>" is entered to the form
      Then the form contains new user "<firstname>" 
      And  the form contains new user "<lastname>"

      Examples:
        | firstname | lastname |
        | Donald    | Duck     |
        | Peter     | Pan      |
        | Lion      | King     |


  Scenario: Clear registration form
      When initial values from form are cleared
      Then the form fields are empty


  Scenario Outline: Submit registration form
      When new "<firstname>" is entered to the form
      And new "<lastname>" is entered to the form
      And submit button is clicked
      Then the form contains initial values

      Examples:
        | firstname | lastname |
        | Donald    | Duck     |
