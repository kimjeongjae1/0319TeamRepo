import re
from random import randrange
import time
import os
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.review_page import ReviewPage

''''

'''

@pytest.mark.skip(reason='테스트중')
@pytest.mark.usefixtures('driver')
class TestTC007:
    
    @pytest.mark.parametrize('KEYWORD', ['자켓'])
    def test_search_filter(self, driver, KEYWORD):    
        wait = WebDriverWait(driver, 10)
        review_page = ReviewPage(driver)
        try:
            review_page.move_main()
            review_page.sleep_random()
            
            review_page.click_xpath(
                review_page.get_right_review_page_icon()
            )

            review_page.sleep_random()

            review_page.switch_to_iframe()  # 필수

            review_page.search_items_filtering(KEYWORD)

            review_page.switch_back_from_iframe()  # 필수

            assert review_page.is_product_name_contains(KEYWORD)
            

        except NoSuchElementException as e:
            driver.save_screenshot('요소 없음.png')
            assert False


    @pytest.mark.skip(reason='테스트중')
    @pytest.mark.parametrize('KEYWORD', 
                             [
                                 'TOP', 
                                # 'BLOUSE&SHIR', 
                                # 'DRESS', 
                                # 'PANTS', 
                                # 'SKIRT', 
                                # 'OUTER', 
                                # 'BAG&SHOES', 
                                # 'ACC', 
                                # 'INNER&SEASON'
                              ]
                              )
    @pytest.mark.skip(reason='테스트중')
    def test_category_filter(self, driver, KEYWORD):    
        wait = WebDriverWait(driver, 10)
        review_page = ReviewPage(driver)
        compare_keyword = ''
        try:
            review_page.move_main()
            # wait.until(
            #     EC.presence_of_element_located(
            #         # main element wait...
            #     )
            # )
            review_page.sleep_random()
            
            # 리뷰 페이지 진입
            review_page.click_xpath(
                review_page.get_right_review_page_icon()
            )

            review_page.sleep_random()

            review_page.switch_to_iframe()  # 필수

            # 카테고리 클릭
            review_page.click_xpath(
                review_page.get_category_filter()
            )

            review_page.sleep_random()

            # 카테고리 속성 클릭
            review_page.click_xpath(
                review_page.get_category_filter_element_keyword(KEYWORD)
            )

            review_page.switch_back_from_iframe()  # 필수

            # 필터링 된 제품 이미지 클릭
            review_page.click_xpath(
                review_page.get_review_product(0)
            )

            review_page.sleep_random()

            compare_keyword = review_page.get_find_element(
                review_page.get_product_category_map()
            ).text
            
            assert KEYWORD == compare_keyword
            

        except NoSuchElementException as e:
            driver.save_screenshot('요소 없음.png')
            assert False

    @pytest.mark.skip(reason='테스트중')
    @pytest.mark.parametrize('RANGE_FILTER', 
                             [
                                 '1만원 이하', 
                                # '1만원 ~ 3만원', 
                                # '3만원 ~ 5만원', 
                                # '5만원 ~ 10만원', 
                                # '10만원 이상', 
                              ]
                              )
    @pytest.mark.skip(reason='테스트중')
    def test_price_range_filter(self, driver, RANGE_FILTER):
        wait = WebDriverWait(driver, 10)
        review_page = ReviewPage(driver)

        price = ''
        range_min = float('inf')
        range_max = 0
        
        try:
            review_page.move_main()
            # wait.until(
            #     EC.presence_of_element_located(
            #         # main element wait...
            #     )
            # )
            review_page.sleep_random()
            
            # 리뷰 페이지 진입
            review_page.click_xpath(
                review_page.get_right_review_page_icon()
            )

            review_page.sleep_random()


            review_page.switch_to_iframe()  # 필수


            # 가격대 선택 클릭
            review_page.click_xpath(
                review_page.get_price_range_filter()
            )

            review_page.sleep_random()


            # 가격대 클릭
            if RANGE_FILTER == '1만원 이하':
                range_min = 0
                range_max = 10000
                review_page.click_xpath(
                    review_page.get_price_range_filter_under_1()
                )
            elif RANGE_FILTER == '1만원 ~ 3만원':
                range_min = 10000
                range_max = 30000
                review_page.click_xpath(
                    review_page.get_price_range_filter_1_3()
                )
            elif RANGE_FILTER == '3만원 ~ 5만원':
                range_min = 30000
                range_max = 50000
                review_page.click_xpath(
                    review_page.get_price_range_filter_3_5()
                )
            elif RANGE_FILTER == '5만원 ~ 10만원':
                range_min = 50000
                range_max = 100000
                review_page.click_xpath(
                    review_page.get_price_range_filter_5_10()
                )
            elif RANGE_FILTER == '10만원 이상':
                range_min = 10000
                range_max = float('inf')
                review_page.click_xpath(
                    review_page.get_price_range_filter_over_10()
                )

            review_page.switch_back_from_iframe()

            # 필터링 된 제품 이미지 클릭
            review_page.click_xpath(
                review_page.get_review_product(0)
            )

            review_page.sleep_random()

            price = review_page.get_find_element(
                review_page.get_product_price_sell_price()
            ).text

            price = int(re.sub(r'[^0-9]', '', price))  # 숫자만 남기고 전부 지우기

            if RANGE_FILTER == '10만원 이상':
                assert range_min <= price
            elif RANGE_FILTER == '1만원 이하':
                assert price <= range_max
            else:
                assert range_min <= price <= range_max
            

        except NoSuchElementException as e:
            driver.save_screenshot('요소 없음.png')
            assert False

        