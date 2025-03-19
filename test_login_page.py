from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from login_page import LoginPage
from hide import USER_DATA
import logging
import pytest
import time

@pytest.mark.usefixtures("driver")
class TestLoginPage:
    # 회원가입
    #@pytest.mark.skip(reason="아직 테스트케이스 발동 안함")
    def test_signup(self, driver: WebDriver):
        try:
            EVERY_AGREE_NAME = "every_agree"
            AGE_CHECK_NAME = "user_age_check"
            SIGNIN_LINK_TEXT = "동의하고 가입하기"
            SIGNIN_INPUT_XPATH = "//ul/li/label"
            SIGNIN_NAME_ID = "hname"
            SIGNIN_ID_ID = "id"
            SIGNIN_PASSWORD_ID = "password1"
            SIGNIN_PASSWORD_RE_ID = "password2"
            SIGNIN_EMAIL_ID = "email"
            SIGNIN_PHONE_ID = "etcphone"

            login_page = LoginPage(driver)
            login_page.open()

            # 회원가입 페이지 진입
            login_page.click_by_LINK_TEXT('회원가입')
            wait = ws(driver, 5)
            wait.until(EC.url_contains("shop/idinfo.html"))

            assert "shop/idinfo.html" in driver.current_url

            # 회원가입 페이지로 이동
            login_page.click_by_NAME(EVERY_AGREE_NAME)
            login_page.click_by_LINK_TEXT(SIGNIN_LINK_TEXT)

            wait.until(EC.url_contains("shop/idinfo.html"))

            input_cnt = driver.find_elements(By.XPATH, SIGNIN_INPUT_XPATH)

            assert "shop/idinfo.html" in driver.current_url
            assert len(input_cnt) >= 7

            # 회원정보 입력
            login_page.enter_by_ID(SIGNIN_NAME_ID, USER_DATA["name"])
            login_page.enter_by_ID(SIGNIN_ID_ID, USER_DATA["id"])
            login_page.enter_by_ID(SIGNIN_PASSWORD_ID, USER_DATA["password"])
            login_page.enter_by_ID(SIGNIN_PASSWORD_RE_ID, USER_DATA["password"])
            login_page.enter_by_ID(SIGNIN_EMAIL_ID, USER_DATA["email"])
            login_page.enter_by_ID(SIGNIN_PHONE_ID, USER_DATA["phone"])
            login_page.enter_by_select("birthyear")
            login_page.enter_by_select("birthmonth")
            login_page.enter_by_select("birthdate")
            login_page.click_by_NAME(AGE_CHECK_NAME)
            time.sleep(1)

            # 회원가입 버튼 클릭
            login_page.click_signin_btn()
            time.sleep(5)

            # 얼럿 확인
            Alert(driver).accept()
            time.sleep(3)
            wait.until(EC.url_contains("shop/idinfo.html"))
            prod_list = driver.find_elements(By.XPATH, '//ul[@class="info prd_list"]/li')

            assert len(prod_list) > 0
            assert "REGO" in driver.current_url
            
        except NoSuchElementException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot ("로그인페이지_회원가입_실패_NoSuchElementException.png")
            assert False

        except TimeoutException as e:
            logging.exception(f"error: {e}")
            driver.save_screenshot ("로그인페이지_회원가입_실패_TimeoutException.png")

    # 로그인
    @pytest.mark.skip(reason="아직 테스트케이스 발동 안함")
    def test_login(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()

            # 회원정보 입력
            login_page.login()
            time.sleep(3)

            wait = ws(driver, 5)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "로그아웃")))
            time.sleep(2)
            top_btn = driver.find_elements(By.XPATH, '//ul[@class="top_info"]/li/a')

            assert "mainm.html" in driver.current_url
            assert len(top_btn) == 6

        except NoSuchElementException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot ("로그인페이지_로그인_실패_NoSuchElementException.png")
            assert False

        except TimeoutException as e:
            logging.exception(f"error: {e}")
            driver.save_screenshot ("로그인페이지_로그인_실패_TimeoutException.png")