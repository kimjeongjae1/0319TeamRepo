from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class LikePage:

    # 생성자에서 driver 초기화
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # WebDriverWait 기본 타임아웃: 10초

    # 상품 페이지에서 관심 상품 등록
    def add_likeitem(self):
        likebtn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='info']/div[2]/a[3]")))
        likebtn.click()

        alert = self.wait.until(EC.alert_is_present())  # Alert 창 대기
        alert.accept()

    # 관심 상품 등록 검증
    def verify_likeitem(self):
    # 관심 상품 페이지 열기
    

        # 관심 상품 페이지에서 "보관하신 상품 내역이 없습니다." 메시지를 확인
        empty_message = self.driver.find_elements(By.CLASS_NAME, "tb-center")

        # "보관하신 상품 내역이 없습니다." 메시지가 있다면 상품이 담기지 않은 상태
        if len(empty_message) > 0 and "보관하신 상품 내역이 없습니다." in empty_message[0].text:
            assert False, "검증 실패: 관심 상품이 등록되지 않았습니다."

        # 메시지가 없으면 상품이 담겨 있는 상태
        print("검증 성공: 관심 상품이 등록되었습니다.")


    # 관심 상품 페이지 접근
    def open_wishlist(self):
        # 마이페이지 접근
        mypageopen = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='hd']/div[1]/div/ul/li[2]/a")))
        mypageopen.click()

        # 관심 상품 페이지 접근
        wishopen = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ImageMapsCom-image-maps-2018-10-14-232204']/area[3]")))
        wishopen.click()

    # 관심 상품 삭제
    def delete_wish(self):
        # 관심 상품 삭제 버튼 클릭
        wishdelete = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='myWish']/div[2]/div[1]/table/tbody/tr/td[7]/div/a[2]")))
        wishdelete.click()

        # Alert 창 대기 및 승인
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

        # "보관하신 상품 내역이 없습니다." 메시지가 나타날 때까지 대기
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tb-center")))


    # 관심 상품 삭제 검증
    def verify_wish_deleted(self):
        # "보관하신 상품 내역이 없습니다." 메시지를 확인
        empty_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tb-center"))).text

        # 메시지가 "보관하신 상품 내역이 없습니다."인지 확인
        if "보관하신 상품 내역이 없습니다." in empty_message:
            print("검증 성공: 관심 상품이 삭제되었습니다.")
        else:
            raise AssertionError("검증 실패: 관심 상품이 삭제되지 않았습니다.")
