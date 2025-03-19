from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
from Pages.like_page import LikePage  # like_page.py 파일에 저장된 걸 불러옴

# 웹드라이버 실행 (Chrome 기준)
driver = webdriver.Chrome()

try:
    # 쇼핑몰 페이지 접속
    driver.get("https://www.nibbuns.co.kr/shop/shopdetail.html?branduid=72185&xcode=026&mcode=004&scode=&type=Y&sort=manual&cur_code=026&GfDT=bGx3UQ%3D%3D")
    driver.maximize_window()

    # LikePage 클래스 인스턴스 생성
    like_page = LikePage(driver)

    # 관심 상품 등록 테스트
    like_page.add_likeitem()
    time.sleep(2)

    # 관심 상품 페이지 열기
    like_page.open_wishlist()
    time.sleep(2)

    # 관심 상품 삭제 테스트
    like_page.delete_wish()
    time.sleep(2)

    # 스크린샷 저장
    driver.save_screenshot("like_test_result.png")
    print("🎉 테스트 완료! 스크린샷이 저장되었습니다.")

except Exception as e:
    print(f"❗ 오류 발생: {e}")

finally:
    # 웹드라이버 종료
    driver.quit()