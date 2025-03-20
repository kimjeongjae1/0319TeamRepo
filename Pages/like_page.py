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

    #관심 상품 등록 검증
    def verify_likeitem(self):
        

        # "보관중인 상품 내역이 없습니다."라는 문구 확인
        empty_message = self.driver.find_elements(By.CLASS_NAME, "tb-center")  

        # 빈 상태 메시지가 존재하지 않을 경우 검증 통과
        assert len(empty_message) == 0, "검증 실패: 관심 상품이 등록되지 않았습니다."

    #관심 상품 페이지 접근
    def open_wishlist(self):
        #마이페이지 우선 접근
        mypageopen = self.driver.find_element(By.XPATH,"//*[@id='hd']/div[1]/div/ul/li[2]/a")
        mypageopen.click()

        time.sleep(2)


        #관심상품 페이지 접근
        wishopen = self.driver.find_element(By.XPATH,"//*[@id='ImageMapsCom-image-maps-2018-10-14-232204']/area[3]")
        wishopen.click()

    #관심 상품 페이지 검증
    def verify_wishlist_open(self):
        current_url = self.driver.current_url
        assert "wishlist" in current_url, "관심 상품 페이지 열기 실패: URL이 예상과 다릅니다."


    #관심 상품 삭제 
    def delete_wish(self):
        wishdelete = self.driver.find_element(By.XPATH, "//*[@id='myWish']/div[2]/div[1]/table/tbody/tr/td[7]/div/a[2]")
        wishdelete.click()

        time.sleep(1)

        # Alert 창에 접근해서 확인 버튼 누르기
        alert = Alert(self.driver)
        alert.accept()

    def verify_wish_deleted(self):
        # 관심 상품 페이지에서 빈 상태 메시지 확인
        empty_message = self.driver.find_element(By.CLASS_NAME, "tb-center").text 

        # 빈 상태 메시지가 "보관중인 상품 내역이 없습니다."인지 확인
        assert "보관중인 상품 내역이 없습니다." in empty_message, "검증 실패: 관심 상품이 삭제되지 않았습니다."
        