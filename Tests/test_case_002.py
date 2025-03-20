from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from login_page import LoginPage
from Pages.search_page import SearchPage
from Pages.cart_page import CartPage
from prod_page import ProdPage
from hide import USER_DATA
import logging
import pytest
import time


class TestScenarioTC:
    def test_scenario(self, driver:WebDriver):
        try:
            login_page = LoginPage(driver)
            search_page = SearchPage(driver)
            prod_page = ProdPage(driver)
            cart_page = CartPage(driver)
            wait = ws(driver, 10)

            # step1 로그인
            login_page.open()
            login_page.login()
            time.sleep(3)

            wait = ws(driver, 5)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "로그아웃")))
            time.sleep(2)
            top_btn = driver.find_elements(By.XPATH, '//ul[@class="top_info"]/li/a')

            assert "mainm.html" in driver.current_url
            assert len(top_btn) == 6

            # step2 상품 페이지 진입
            search_page.random_choice()
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "thumb-info")))

            assert "branduid" in driver.current_url
            driver.save_screenshot('상품-랜덤클릭-상세페이지-성공.jpg')
            time.sleep(5)

            # step3 옵션 1, 2 추가 > 1 삭제, 수량추가 2 > 수량 감소 1
            prod_page.select_option("1")
            prod_page.select_option("2")
            time.sleep(1)

            prod_page.delete("1")
            time.sleep(1)
            add_quantity = 1
            minus_quantity  = 1

            prod_page.quantity_change("plus", add_quantity)
            price_tot = driver.find_element(By.ID, "MK_p_total").text
            price_tot_num = price_tot.replace(",", "").replace("원", "")

            unit_price = driver.find_element(By.XPATH, '//*[@id="info"]/div[1]/table/tbody/tr[2]/td/div').text
            unit_price_int = int(unit_price.replace(",", "").replace("원", ""))
            current_quantity = add_quantity + 1

            assert int(price_tot_num) == unit_price_int * (add_quantity + 1)
            time.sleep(2)

            prod_page.quantity_change("minus", minus_quantity)
            price_tot = driver.find_element(By.ID, "MK_p_total").text
            price_tot_num = price_tot.replace(",", "").replace("원", "")

            unit_price = driver.find_element(By.XPATH, '//*[@id="info"]/div[1]/table/tbody/tr[2]/td/div').text
            unit_price_int = int(unit_price.replace(",", "").replace("원", ""))
            current_quantity -= minus_quantity

            assert int(price_tot_num) == unit_price_int * (current_quantity)
            time.sleep(2)

            # step4 장바구니 페이지 접근
            prod_page.add_cart()
            # 0320김혜영 : 여기까지 테스트 완료

            # step5 담겨있는 수량 변경
            # 총 구매 금액 가져오기
            total_price_element = driver.find_element(By.XPATH, "//*[@id='cartWrap']/div[2]/div[1]/table/tfoot/tr/td/div/strong")  
            initial_total_price = int(total_price_element.text.replace(",", "").replace("원", ""))

            # 상품 단가 가져오기
            unit_price_element = driver.find_element(By.XPATH, "//*[@id='cartWrap']/div[2]/div[1]/table/tbody/tr/td[6]/div")
            unit_price = int(unit_price_element.text.replace(",", "").replace("원", ""))

            # 수량 추가 테스트
            cart_page.add_count()
            time.sleep(2)

            #수량 확인
            cart_page.count_request()

            # 추가 후 총 금액 검증
            updated_total_price_element = driver.find_element(By.XPATH, "//*[@id='cartWrap']/div[2]/div[1]/table/tfoot/tr/td[6]/strong")
            updated_total_price = int(updated_total_price_element.text.replace(",", "").replace("원", ""))
            assert updated_total_price == initial_total_price + unit_price, "❌ 수량 추가에 따른 총 금액 증가 검증 실패"

            # 수량 감소 테스트
            cart_page.minus_count()
            time.sleep(2)

            #수량 확인
            cart_page.count_request()
            time.sleep(2)

            # 감소 후 총 금액 검증
            final_total_price_element = driver.find_element(By.XPATH, "//*[@id='cartWrap']/div[2]/div[1]/table/tfoot/tr/td[6]/strong")
            final_total_price = int(final_total_price_element.text.replace(",", "").replace("원", ""))
            assert final_total_price == updated_total_price - unit_price, "❌ 수량 감소에 따른 총 금액 감소 검증 실패"

            print("🎉 테스트 성공: 수량 변경에 따른 총 금액 변화가 올바르게 반영됩니다.")



        except NoSuchElementException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot ("로그인페이지_회원가입_실패_NoSuchElementException.png")
            assert False

        except TimeoutException as e:
            logging.exception(f"error: {e}")
            driver.save_screenshot ("로그인페이지_회원가입_실패_TimeoutException.png")
