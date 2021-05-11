from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Sniper:
    def __init__(self, sku: str = None):
        self.sku = sku if sku != None else "6430620"

    def returnUrl(self):
        return f"https://www.bestbuy.com/site/{self.sku}.p?skuId={self.sku}"
