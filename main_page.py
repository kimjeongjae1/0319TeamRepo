from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


class MainPage:
    URL = "https://www.nibbuns.co.kr/"
    SEARCH_INPUT_NAME = "MS_search_word"
    SEARCH_BUTTON_CLASS = "btn_srch"

    #객체 > 인스턴스화 setup
    def __init__(self,driver:WebDriver):
        self.driver = driver
    # 메인 페이지 열기
    def open(self):
        self.driver.get(self.URL)

    def search_items(self, item_name: str):
        wait = ws(self.driver, 10)

        # 검색 입력창 찾기
        search_input_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.SEARCH_INPUT_NAME)))
        search_input_box.clear()
        search_input_box.send_keys(item_name)

        # 검색 버튼 클릭
        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.SEARCH_BUTTON_CLASS)))
        search_button.click()


    



   