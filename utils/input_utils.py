from selenium import webdriver
from constants import waits
from time import sleep
from random import randint

def human_type(driver, elem, text):
    for character in text:
        actions = webdriver.ActionChains(driver)
        actions.move_to_element(elem)
        elem.click()
        actions.send_keys(character)
        actions.perform()

def rand_wait_fast():
    sleep(randint(*waits['fast']['interval']))
