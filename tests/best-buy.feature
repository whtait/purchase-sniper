Feature: Best buy search
Scenario: Search for product on best buy
    Given I am on the BestBuy homepage
    When I enter search for "Bees"
    Then Search results for "Bees" should appear

Scenario: Say hello to you
    Given I am on the BestBuy homepage
    When I call hello "there"
    Then "Hello, there!" should be returned
