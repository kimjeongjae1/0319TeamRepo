from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from prod_page import ProdPage
import logging
import pytest
import time

@pytest.mark.usefixtures("driver")
class TestProdPage:
    # 장바구니 담기
    @pytest.mark.skip(reason="아직 테스트케이스 발동 안함")
    def test_add_cart(self, driver: WebDriver):
        try:
            # 상품 페이지 진입
            prod_page = ProdPage(driver)
            prod_page.open()

            wait = ws(driver, 5)
            wait.until(EC.url_contains("shopdetail"))

            assert "shopdetail" in driver.current_url

            # 옵션 선택
            prod_page.select_option("2")    # 아이보리 F
            time.sleep(1)

            # 장바구니에 추가
            prod_page.add_cart()
            wait.until(EC.url_contains("basket"))  

            # 제품페이지 제목이 장바구니에 있는지 확인
            titles_in_cart = driver.find_elements(By.XPATH, '//a[@class="tb-bold"]')
            titles = []
            for title in titles_in_cart:
                titles.append(title.text)

            assert "[니쁜스단독20%할인][프리미엄퀄리티] 부클 하프 트위드 자켓" in titles

            # 제품페이지 가격이 장바구니와 같은지 확인
            cart_pge_price_tot = driver.find_element(By.XPATH, '//div[contains(@class, "tb-price")]/span').text
            cart_pge_price = cart_pge_price_tot.replace(",", "")

            assert int(cart_pge_price) == 99000

        except NoSuchElementException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot ("제품페이지_장바구니_담기_실패_NoSuchElementException.png")
            assert False

        except TimeoutException as e:
            logging.exception(f"error: {e}")
            driver.save_screenshot ("제품페이지_장바구니_담기_실패_TimeoutException.png")

    #@pytest.mark.skip(reason="아직 테스트케이스 발동 안함")
    def test_change_options(self, driver: WebDriver):
        try:
            # 상품 페이지 진입
            prod_page = ProdPage(driver)
            prod_page.open()

            wait = ws(driver, 5)
            wait.until(EC.url_contains("shopdetail"))

            assert "shopdetail" in driver.current_url

            # 옵션 선택
            prod_page.select_option("2")    # 아이보리 F
            time.sleep(1)

            # 옵션 변경
            prod_page.select_option("1") # 블랙 L
            time.sleep(1)
            prod_page.delete("2")
            time.sleep(1)

            selected_option = driver.find_element(By.XPATH, '//div/ul/li/span[@class="MK_p-name"]')
            assert selected_option.text == "블랙 L"
            time.sleep(2)

            # 수량 5증가
            prod_page.quantity_change("plus", 5)
            price_tot = driver.find_element(By.ID, "MK_p_total").text
            price_tot_num = price_tot.replace(",", "").replace("원", "")

            assert int(price_tot_num) == 594000
            time.sleep(2)

            # 수량 4 감소
            prod_page.quantity_change("minus", 4)
            price_tot = driver.find_element(By.ID, "MK_p_total").text
            price_tot_int = int(price_tot.replace(",", "").replace("원", ""))

            assert price_tot_int == 198000
            time.sleep(2)    
            
        except NoSuchElementException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot ("제품페이지_옵션변경_실패_NoSuchElementException.png")
            assert False

        except TimeoutException as e:
            logging.exception(f"error: {e}")
            driver.save_screenshot ("제품페이지_옵션변경_실패_TimeoutException.png")