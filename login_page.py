from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pyperclip import copy, paste
from hide import USER_DATA
import time

class LoginPage:
    url = "https://www.nibbuns.co.kr/shop/member.html?type=login"

    # 객체 인스턴스화를 위한 세팅, 파이테스트의 'driver'를 받아 driver 객체에 넣는다.
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 메인 페이지 열기
    def open(self):
        self.driver.get(self.url)

    # 버튼 클릭
    def click_by_LINK_TEXT(self, link_text: str):
        button = self.driver.find_element(By.LINK_TEXT, link_text)
        button.click()

    # 회원가입 체크박스 클릭
    def click_by_NAME(self, input_name: str):
        input = self.driver.find_element(By.NAME, input_name)
        input.click()

    # 회원가입 텍스트 입력
    def enter_by_ID(self, input_id: str, keys: str):
        input = self.driver.find_element(By.ID, input_id)
        input.send_keys(keys)
    
    # 회원가입 드롭다운리스트 입력
    def enter_by_select(self, name:str):
        select_elem = self.driver.find_elements(By.XPATH, '//dl/dd/select')
        for element in select_elem:
            if element.get_attribute("name") == name:
                Select(element).select_by_value(USER_DATA[name])
                break

    # 회원가입 버튼 클릭
    def click_signin_btn(self):
        button = self.driver.find_element(By.XPATH, '//div[@class="bottom-btn"]/a/img')
        button.click()

    # 로그인
    def login(self):
        id = self.driver.find_element(By.NAME, "id")
        user_id = USER_DATA["id"]
        for text in user_id:
            id.send_keys(text)
            time.sleep(0.2)

        pw = self.driver.find_element(By.NAME, "passwd")
        copy(USER_DATA["password"])
        pw.send_keys(paste())
        
        time.sleep(2)
        pw.send_keys(Keys.ENTER)
