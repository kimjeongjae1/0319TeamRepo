from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
from Pages.like_page import LikePage  # like_page.py 파일에 저장된 걸 불러옴

# 웹드라이버 실행 (Chrome 기준)
driver = webdriver.Chrome()
def test_likeitem():
    try:
        print("테스트 시작: 쇼핑몰 페이지 접속")
        driver.get("https://www.nibbuns.co.kr/shop/shopdetail.html?branduid=72185&xcode=026&mcode=004&scode=&type=Y&sort=manual&cur_code=026&GfDT=bGx3UQ%3D%3D")
        driver.maximize_window()

        print("테스트 단계 1: LikePage 클래스 인스턴스 생성")
        like_page = LikePage(driver)

        print("테스트 단계 2: 관심 상품 등록 테스트")
        like_page.add_likeitem()

        print("테스트 단계 3: 관심 상품 페이지 열기")
        like_page.open_wishlist()

        print("테스트 단계 4: 관심 상품 등록 검증")
        like_page.verify_likeitem()

        print("테스트 단계 5: 관심 상품 삭제 테스트")
        like_page.delete_wish()

        print("테스트 단계 6: 관심 상품 삭제 검증")
        like_page.verify_wish_deleted()

        print("🎉 테스트 완료: 모든 검증 통과!")

    except Exception as e:
        print(f"❗ 오류 발생: {e}")

    finally:
        driver.quit()