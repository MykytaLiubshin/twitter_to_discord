import os


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

from utils.input_utils import human_type
from utils.get_driver import get_driver

TWITTER_LINK = "https://twitter.com"
MIRRA = "/mirraqpow"
MIRRA_TWITTER = TWITTER_LINK + MIRRA

def run():
    
    with get_driver() as  driver:
        driver.get(NEW_LINK)
        
        sleep(1000)

if __name__ == '__main__':
    run()