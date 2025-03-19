from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from Pages.cart_page import CartPage  # cart_page.py 파일에 저장된 걸 불러옴

# 웹드라이버 실행 (Chrome 기준)
driver = webdriver.Chrome()

try:
    #쇼핑몰 페이지 접속
    driver.get("https://www.nibbuns.co.kr/shop/shopbrand.html")
    driver.maximize_window()

    #CartPage 클래스 인스턴스 생성
    cart_page = CartPage(driver)

    #장바구니 페이지 열기
    cart_page.cartpage_open()
    time.sleep(2)

    #수량 추가 테스트
    cart_page.add_count()
    time.sleep(1)

    #수량 변경 확인 버튼 클릭
    cart_page.count_request()
    time.sleep(2)

    #수량 감소 테스트
    cart_page.minus_count()
    time.sleep(1)

    #수량 변경 확인 버튼 클릭
    cart_page.count_request()
    time.sleep(2)

    #장바구니 상품 삭제 테스트
    cart_page.item_delete()
    time.sleep(2)

    # 스크린샷 저장 
    driver.save_screenshot("cart_test_result.png")
    print("🎉 테스트 완료! 스크린샷이 저장되었습니다.")

except Exception as e:
    print(f"❗ 오류 발생: {e}")

finally:
    # 웹드라이버 종료
    driver.quit()