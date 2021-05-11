Feature: The bot can navigate BestBuy's website.

Scenario: I am searching for a specific SKU.
    Given I provide the SKU "6430620".
    When I instantiate the class with the SKU.
    Then I am given a custom URL "https://www.bestbuy.com/site/6430620.p?skuId=6430620" linking to the product page.
