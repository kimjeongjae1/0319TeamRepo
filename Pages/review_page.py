from random import randrange
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class ReviewPage():
    _MAIN_URL = "https://www.nibbuns.co.kr/"
    # 메인페이지 우측 메뉴 -> 리뷰 페이지 진입 아이콘
    _right_review_page_icon = "//div[@id='aside']/div[@class='right close ']/ul[@class='second']/li[4]/a/img"
    # 검색 필터 입력창
    _search_filter_input = "//input[@id='search_keyword']"
    
    # 검색 필터 돋보기 아이콘
    _search_filter_icon = "//div[@class='price_list catedesign']/div[@class='text_box_button catedesign']/img"
    # 카테고리 선택 필터
    _category_filter = "//div[@id='selected_cate']"
    # 카테고리 필터 세부 선택_
    def get_category_filter_element_keyword(self, filter_kw):
        # filter_kw 리스트
        # TOP, BLOUSE&SHIR, DRESS, PANTS, SKIRT, OUTER, BAG&SHOES, ACC, INNER&SEASON
        return f"(//div[@class='sf_review_filter_list catedesign']/div[@class='sf_review_filter']/span[contains(text(), {filter_kw})])[1]"
    # 가격대 선택 필터
    _price_range_filter = "//div[@id='selected_price']/span"
    # 가격대 선택 필터 -> 1만원 이하
    _price_range_filter_under_1 = "//div[@class='sf_review_filter_list catedesign']/div[@class='sf_review_filter']/span[contains(text(), '1만원 이하')]"
    # 가격대 선택 필터 -> 1만원 ~ 3만원
    _price_range_filter_1_3 = "//div[@class='sf_review_filter_list catedesign']/div[@class='sf_review_filter']/span[contains(text(), '1만원 ~ 3만원')]"
    # 가격대 선택 필터 -> 3만원 ~ 5만원
    _price_range_filter_3_5 = "//div[@class='sf_review_filter_list catedesign']/div[@class='sf_review_filter']/span[contains(text(), '3만원 ~ 5만원')]"
    # 가격대 선택 필터 -> 5만원 ~ 10만원
    _price_range_filter_5_10 = "//div[@class='sf_review_filter_list catedesign']/div[@class='sf_review_filter']/span[contains(text(), '5만원 ~ 10만원')]"
    # 가격대 선택 필터 -> 10만원 이상
    _price_range_filter_over_10 = "//div[@class='sf_review_filter_list catedesign']/div[@class='sf_review_filter']/span[contains(text(), '10만원 이상')]"
    # 리뷰 상품 이미지
    def get_review_product(self, index):
        # 리뷰 상품 이미지
        return f"(//div[@class='sf_review_area']/div[@class='sf_review_user_info set_report'])[{index+1}]/div[@class='sf_review_item_thumb sf_review_main_img_area']/img"
    # 리뷰 모든 상품명 다 가져오기
    _all_product_name = "//div[@class='sf_review_area']/div/div[@class='sf_review_item_info_detail']/div[@class='sf_review_item_namearea']/span"

    '''
    상품 상세페이지
    '''
    # 상품 분류 > 상품 분류 마지막 가져오기
    _product_category_map = "//div[@id='productDetail']/div[@class='loc-navi']/div[@class='loc-r']/a[last()]"
    # 상품 클릭 -> 상품 할인가 가져오기
    _product_price_sell_price = "//td[@class='price sell_price']/div[@class='tb-left']"

    def get_MAIN_URL(self):
        return self._MAIN_URL
    
    def get_right_review_page_icon(self):
        # 메인페이지 우측 메뉴 -> 리뷰 페이지 진입 아이콘\
        return self._right_review_page_icon
    
    def get_search_filter_input(self):
        # 검색 필터 입력창
        return self._search_filter_input
    
    def get_search_filter_icon(self):
        # 검색 필터 돋보기 아이콘
        return self._search_filter_icon
    
    def get_category_filter(self):
        # 카테고리 선택 필터
        return self._category_filter
    
    def get_price_range_filter(self):
        # 가격대 선택 필터
        return self._price_range_filter
    
    def get_price_range_filter_under_1(self):
        # 가격대 선택 필터 -> 1만원 이하
        return self._price_range_filter_under_1
    
    def get_price_range_filter_1_3(self):
        # 가격대 선택 필터 -> 1만원 ~ 3만원
        return self._price_range_filter_1_3
    
    def get_price_range_filter_3_5(self):
        # 가격대 선택 필터 -> 3만원 ~ 5만원
        return self._price_range_filter_3_5
    
    def get_price_range_filter_5_10(self):
        # 가격대 선택 필터 -> 5만원 ~ 10만원
        return self._price_range_filter_5_10
    
    def get_price_range_filter_over_10(self):
        # 가격대 선택 필터 -> 10만원 이상
        return self._price_range_filter_over_10
    
    def get_all_product_name(self):
        # 리뷰 모든 상품명 다 가져오기
        return self._all_product_name
    
    def get_product_category_map(self):
        # 상품 상세페이지
        # 상품 분류 > 상품 분류 마지막 가져오기
        return self._product_category_map
    
    def get_product_price_sell_price(self):
        # 상품 상세페이지
        # 상품 클릭 -> 상품 할인가 가져오기
        return self._product_price_sell_price
    
    
 

    def __init__(self, driver:WebDriver):
        self.driver = driver

    def click_xpath(self, xpath:str) -> None:
        self.driver.find_element(By.XPATH, xpath).click()
    
    def clear_xpath(self, xpath:str) -> None:
        self.driver.find_element(By.XPATH, xpath).clear()

    def sleep_random(self) -> None:
        time.sleep((randrange(10, 30))*0.01)

        # 메인 페이지 열기
    def move_main(self) -> None:
        self.driver.get(self.get_MAIN_URL())

    def switch_to_iframe(self) -> None:
        wait = WebDriverWait(self.driver, 10)
        iframe = wait.until(
            EC.presence_of_element_located(
                (By.ID, 'review_widget1001_0')
            )
        )
        self.driver.switch_to.frame(iframe)  # 돔 전환
    
    def switch_back_from_iframe(self) -> None:
        self.driver.switch_to.default_content()
    
    def search_items_filtering(self, product_name:str) -> None:
        wait = WebDriverWait(self.driver, 10)

        self.sleep_random()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, self.get_search_filter_input())
            )
        )
        
        search_input_box = self.driver.find_element(By.XPATH, self.get_search_filter_input())
        search_input_box.click()
        search_input_box.send_keys(product_name)
        search_input_box.send_keys(Keys.ENTER)

        

    def get_find_element(self, element):
        return self.driver.find_element(element)

    def is_product_name_contains(self, keyword:str) -> bool:
        
        product_names = self.driver.find_elements(By.XPATH, self.get_all_product_name())
        for p_name in product_names:
            p_name = p_name.text
            if keyword not in p_name:
                return False
        return True
