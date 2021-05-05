#Python Behave testing example for Selenium test automation
# from selenium import webdriver
# import os
# from configparser import ConfigParser
# from selenium.webdriver.common.keys import Keys
# import time
# from behave import given, when, then
 
@given('I am on the BestBuy homepage')
def step(context):
    # context.helperfunc.open('https://lambdatest.github.io/sample-todo-app/')
    # context.helperfunc.maximize()
    pass
 
@when('I enter search for {product}')
def click_on_checkbox_one(context, product):
    # context.helperfunc.find_by_name('li1').click()
    # context.helperfunc.find_by_name('li2').click()
    pass
 
@then('Search results for {product} should appear')
def enter_item_name(context, product):

    assert product == "Bees"
    # context.helperfunc.find_by_id('sampletodotext').send_keys("Yey, Let's add it to list")
    pass
 
# @when('I click add button')
# def click_on_add_button(context):
#     # context.helperfunc.find_by_id('addbutton').click()
 
# @then('I should verify the added item')
# def see_login_message(context):
#     # added_item = context.helperfunc.find_by_xpath("//span[@class='done-false']").text
#     # time.sleep(10)
#     # if added_item in "Yey, Let's add it to list":
#     #     return True
#     # else:
#     #     return False

