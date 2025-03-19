from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


class LikePage:

    # 생성자에서 driver 초기화
    def __init__(self, driver: webdriver):
        self.driver = driver


    #상품 페이지에서 관심 상품 등록
    def add_likeitem(self):
        likebtn = self.driver.find_element(By.XPATH, "//*[@id='info']/div[2]/a[3]")
        likebtn.click()

        time.sleep(1)

        # Alert 창에 접근해서 확인 버튼 누르기
        alert = Alert(self.driver)
        alert.accept()


    #관심 상품 페이지 접근
    def open_wishlist(self):
        #마이페이지 우선 접근
        mypageopen = self.driver.find_element(By.XPATH,"//*[@id='hd']/div[1]/div/ul/li[2]/a")
        mypageopen.click()

        time.sleep(2)


        #관심상품 페이지 접근
        wishopen = self.driver.find_element(By.XPATH,"//*[@id='ImageMapsCom-image-maps-2018-10-14-232204']/area[3]")
        wishopen.click()


    #관심 상품 삭제 
    def delete_wish(self):
        wishdelete = self.driver.find_element(By.XPATH, "//*[@id='myWish']/div[2]/div[1]/table/tbody/tr/td[7]/div/a[2]")
        wishdelete.click()

        time.sleep(1)

        # Alert 창에 접근해서 확인 버튼 누르기
        alert = Alert(self.driver)
        alert.accept()

    