from utils.get_driver import get_driver
from constants import MIRRA_TWITTER, waits
from utils.input_utils import rand_wait_fast
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from random import choice
def get_waited_by_xpath(driver, waits_mode, xpath):
    return WebDriverWait(driver, waits[waits_mode]["std"]).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
def go_to_twitter_page(driver, link: str = MIRRA_TWITTER):
    driver.get(link)
    rand_wait_fast()
    mode = "fast"
    recent_posts_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div'
    recent_posts_element = get_waited_by_xpath(driver, mode, recent_posts_xpath)
    first_article_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]'
    first_article = WebDriverWait(driver, waits[mode]["std"]).until(
        EC.element_to_be_clickable((By.XPATH, first_article_xpath))
    )
    rand_wait_fast()
    rand_wait_fast()
    rand_wait_fast()

    # first_article.screenshot(f"{[choice(list('qwertyuiop[asdfghjkl;zxcvbnm,.1234567890-=QWERTYUIOPASDFGHJKLZXCVBNM')) for _ in range(20)]}.png")
    recent_posts_element.screenshot("image/test.png")
    print(recent_posts_element)
    print(recent_posts_element.get_attribute('style'))
    print(recent_posts_element.find_element(By.TAG_NAME, 'div'))
