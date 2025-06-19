from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class WebDriverFactory:
    @staticmethod
    def get_driver():
        driver = webdriver.Chrome()
        return driver
    
    @staticmethod
    def get_wait(driver, timeout=15):
        return WebDriverWait(driver, timeout)