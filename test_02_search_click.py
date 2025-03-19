import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from main_page import MainPage
from search_page import SearchPage
from selenium.webdriver.chrome.webdriver import WebDriver 

@pytest.mark.usefixtures("driver")
class TestSerachPage:
    def test_search_page(self,driver:WebDriver):
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

            search_page= SearchPage(driver)
            search_page.set_price_range(10000,30000)
            time.sleep(2)

            prices = []
            for item in items:
                try:
                    price_text = item.find_element(By.CLASS_NAME, "price_sell").text
                    numeric_price = int(price_text.replace(",", "").replace("원", ""))
                    prices.append(numeric_price)
                except Exception as e:
                    print(f"가격 정보를 찾을 수 없는 상품이 있습니다: {e}")

            for price in prices:
                assert 10000 <= price <= 30000, f"가격 {price}원이 범위를 벗어남!"

            driver.save_screenshot('검색페이지-가격-성공.jpg')

            search_page.random_choice()

            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "thumb-info")))

            driver.save_screenshot('상품-랜덤클릭-상세페이지-성공.jpg')


            
        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")