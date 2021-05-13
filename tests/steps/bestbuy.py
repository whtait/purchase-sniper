# Python Behave testing example for Selenium test automation
# from selenium import webdriver
# import os
# from configparser import ConfigParser
# from selenium.webdriver.common.keys import Keys
# import time
# from behave import given, when, then

from src import bestbuy


@given('I provide the SKU "{providedSKU}".')
def provideSku(context, providedSKU: str):
    context.sku = providedSKU
    pass


@when("I instantiate the class with the SKU.")
def instantiateSniperClass(context):
    context.sniper = bestbuy.Sniper(context.sku)


@then('I am given a custom URL "{expected}" linking to the product page.')
def returnUrl(context, expected: str):
    actual = context.sniper.pointToURL()
    assert actual == expected, f"Expected [{expected}] Got [{actual}]"

@then('I expect the returned price to be "{expected}"')
def checkPrice(context, expected: str):
    actual = context.sniper.getProductPrice()
    assert actual == expected, f"Expected [{expected}] Got [{actual}]"
