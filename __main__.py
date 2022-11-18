from asyncio import get_event_loop
from utils.get_driver import get_driver
from utils.sql_util import initialize
from data_gather.twitter_update_checker import go_to_twitter_page
def run():
    event_loop = get_event_loop()
    driver = get_driver()
    go_to_twitter_page(driver)

    # with get_driver() as  driver:
    #     driver.get(NEW_LINK)
        
    #     sleep(1000)

if __name__ == '__main__':
    run()
