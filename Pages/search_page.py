from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.chrome.webdriver import WebDriver
import random



class SearchPage:

    LOW_PRICE_NAME = "money1"
    HIHH_PRICE_NAME = "money2"
    SEARCH_XPATH = "//a[img[@alt='검색하기']]"
    ITEMS_XPATH = "//ul/li"
    PRODUCT_LINK_XPATH = "//ul/li//a[contains(@href, 'shopdetail.html')]"

    #객체 > 인스턴스화 setup
    def __init__(self,driver:WebDriver):
        self.driver = driver
    def set_price_range(self, low_price: str, high_price : str):
        wait = ws(self.driver, 10)

        low_price_box = wait.until(EC.presence_of_element_located((By.NAME, self.LOW_PRICE_NAME)))
        low_price_box.clear()
        low_price_box.send_keys(low_price)

        high_price_box = wait.until(EC.presence_of_element_located((By.NAME, self.HIHH_PRICE_NAME)))
        high_price_box.clear()
        high_price_box.send_keys(high_price)

        search_button =  wait.until(EC.presence_of_element_located((By.XPATH, self.SEARCH_XPATH)))
        search_button.click()

    def random_choice(self):
        wait = ws(self.driver, 10)

        items = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.PRODUCT_LINK_XPATH)))

        random_item = random.choice(items)
        product_link = random_item.get_attribute("href")


        self.driver.get(product_link)

        






    



   