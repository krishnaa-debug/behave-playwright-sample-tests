Feature: Simple Playwright + BrowserStack Test
  Basic test to verify SDK integration

  Scenario: Open and verify a webpage
    Given I launch the browser
    When I navigate to "https://www.google.com"
    Then the page title should contain "Google"
    And I close the browser
