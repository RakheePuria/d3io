Feature: Test D3IO functionality

  Scenario: Validate that a pre-created user is able to login to d3a.io
    Given User navigates to d3io page
    When User enters the credentials with username as "rnrakhee86@gmail.com" and password as "abc@12345"
    Then User clicks submit button
    Then User verifies login success

  Scenario: Validate that a logged in user is able to create a project from this page
    Given User navigates to d3io page
    When User enters the credentials with username as "rnrakhee86@gmail.com" and password as "abc@12345"
    Then User clicks submit button
    Then User creates a project named "FirstProject" after successful login
    Then User validates that the "FirstProject" is created successfully


  Scenario: Validate create simulation on the created project
    Given User navigates to d3io page
    When User enters the credentials with username as "rnrakhee86@gmail.com" and password as "abc@12345"
    Then User clicks submit button
    Then User creates the simulation for the "FirstProject"
    Then User validates the simulation is created successfully
    Then User deletes the project