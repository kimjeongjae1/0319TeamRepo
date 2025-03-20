from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class ProdPage:
    url = "https://www.nibbuns.co.kr/shop/shopdetail.html?branduid=72185&search=&xcode=004&mcode=000&scode=&special=1&GfDT=aGp3UQ%3D%3D"
    QTY_CHANGE_CLASS_NAME = {"plus": "MK_btn-up", "minus": "MK_btn-dw"}
    
    # 객체 인스턴스화를 위한 세팅, 파이테스트의 'driver'를 받아 driver 객체에 넣는다.
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 메인 페이지 열기
    def open(self):
        self.driver.get(self.url)

    # 옵션 선택
    def select_option(self, option_value: str):
        option_element = self.driver.find_element(By.NAME, "optionlist[]")
        Select(option_element).select_by_value(option_value)

    # 수량 증감
    def quantity_change(self, change:str, quantity: int):
        # option = self.driver.find_element(By.XPATH, '//div/ul/li//span[@class="MK_p-name"]')
        plus_element = self.driver.find_element(By.CLASS_NAME, self.QTY_CHANGE_CLASS_NAME[change])
        
        for _ in range(quantity):
            plus_element.click()

    # 옵션삭제
    def delete(self, option: str):
        options = self.driver.find_elements(By.XPATH, '//div/ul/li/span[@class="MK_p-name"]')
        for opt in options:
            print(opt.text)
            if opt.text == option:
                delete_btn = self.driver.find_element(By.XPATH, '//a[contains(@id, "MK_btn_del_basic")]')
                delete_btn.click()

    # 장바구니 담기
    def add_cart(self):
        cart_element = self.driver.find_element(By.ID, "cartBtn")
        cart_element.click()
        continue_element = self.driver.find_element(By.LINK_TEXT, "장바구니 확인")
        continue_element.click()