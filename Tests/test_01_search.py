import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib import parse
from Pages.main_page import MainPage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver 


@pytest.mark.usefixtures("driver")
class TestMainPage:
    def test_main_page(self,driver:WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()
            time.sleep(2)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("nibbuns.co.kr"))
            assert "nibbuns.co.kr" in driver.current_url
            time.sleep(2)

            # 상품 검색 
            ITEMS_XPATH = "//ul/li"
            main_page.search_items('반팔')
            ws(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ITEMS_XPATH))
            )

            items = driver.find_elements(By.XPATH, ITEMS_XPATH)

            assert len(items) > 0
            


            driver.save_screenshot('메인페이지-검색-성공.jpg')
            time.sleep(2)


        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")
