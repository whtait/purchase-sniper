from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import with_tag_name
from dotenv import load_dotenv
import os

load_dotenv()

class Sniper:
    def __init__(self, sku: str = None):
        self.sku = sku if sku != None else "6430620"

    def pointToURL(self):
        return f"https://www.bestbuy.com/site/{self.sku}.p?skuId={self.sku}"

    def getProductPrice(self):
        driver = webdriver.Chrome(os.getenv('chromiumPath'))
        driver.get(self.pointToURL())
        price = driver.findElement(By.cssSelector(".priceView-hero-price")).text
        return price
