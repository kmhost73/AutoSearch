# utils/selenium_driver.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc

def get_stealth_driver():
    options = uc.ChromeOptions()
    options.add_argument('--headless=new')  # Use '--headless=new' for Chrome 109+
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--window-size=1920,1080')

    driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver