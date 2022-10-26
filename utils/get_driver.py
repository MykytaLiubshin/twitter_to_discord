from selenium import webdriver
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import random as r
from webdriver_manager.chrome import ChromeDriverManager
import os

PATH_TO_CHROME = os.path.join('/', 'home', 'mykyta',  '.config', 'google-chrome', 'Default')


def get_driver():
    ua = UserAgent()

    options = Options()

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    return driver
