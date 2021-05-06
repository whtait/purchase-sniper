from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BestBuy:
    def __init__(self, url: str = None):
        self.url = url if url != None else "https://bestbuy.com"

    def hello(self, name: str) -> str:
        return f"Hello, {name}!"
