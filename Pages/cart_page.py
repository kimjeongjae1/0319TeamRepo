from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

class CartPage:

    # 생성자에서 driver 초기화
    def __init__(self, driver: webdriver):
        self.driver = driver

    # 장바구니 페이지 오픈
    def cartpage_open(self):
        cartbtn = self.driver.find_element(By.XPATH, "//*[@id='hd']/div[1]/div/ul/li[4]/a")
        cartbtn.click()

    # 수량 변경 메서드 (수량 추가)
    def add_count(self):
        addcount = self.driver.find_element(By.XPATH, "//*[@id='cartWrap']/div[2]/div[1]/table/tbody/tr/td[4]/div/div/span/a[2]/img")
        addcount.click()

    # 수량 변경 메서드 (수량 감소)
    def minus_count(self):
        minuscount = self.driver.find_element(By.XPATH, "//*[@id='cartWrap']/div[2]/div[1]/table/tbody/tr/td[4]/div/div/span/a[1]/img")
        minuscount.click()

    # 수량 변경 확인버튼 클릭 메서드
    def count_request(self):
        requestbtn = self.driver.find_element(By.XPATH, "//*[@id='cartWrap']/div[2]/div[1]/table/tbody/tr/td[4]/div/a")
        requestbtn.click()

    # 장바구니 상품 삭제 기능
    def item_delete(self):
        itemdeletebtn = self.driver.find_element(By.XPATH, "//*[@id='cartWrap']/div[2]/div[1]/table/tbody/tr/td[8]/div/span[2]/a")
        itemdeletebtn.click()

        time.sleep(1)

        # Alert 창에 접근해서 확인 버튼 누르기
        alert = Alert(self.driver)
        alert.accept()  

