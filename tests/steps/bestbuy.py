# Python Behave testing example for Selenium test automation
# from selenium import webdriver
# import os
# from configparser import ConfigParser
# from selenium.webdriver.common.keys import Keys
# import time
# from behave import given, when, then

from src import bestbuy


@given("I am on the BestBuy homepage")
def step(context):
    context.Sniper = bestbuy.Sniper()
    pass


@when('I enter search for "{product}"')
def click_on_checkbox_one(context, product: str):
    pass


@then('Search results for "{product}" should appear')
def enter_item_name(context, product: str):
    assert product == "Bees"
    pass


@when('I call hello "{name}"')
def step_impl(context, name: str):
    context.result = context.Sniper.hello(name)


@then('"{expected}" should be returned')
def step_impl(context, expected: str):
    assert context.result == expected, f"Expected [{expected}] Got [{context.result}]"
