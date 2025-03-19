from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Pages.cart_page import CartPage  # cart_page.py 파일 임포트

# 웹드라이버 실행
driver = webdriver.Chrome()

try:
    # 쇼핑몰 페이지 접속
    driver.get("https://www.nibbuns.co.kr/shop/shopbrand.html")
    driver.maximize_window()

    # CartPage 클래스 인스턴스 생성
    cart_page = CartPage(driver)

    # 장바구니 페이지 열기
    cart_page.cartpage_open()
    time.sleep(2)

    # 총 구매 금액 가져오기
    total_price_element = driver.find_element(By.XPATH, "//*[@id='cartWrap']/div[2]/div[1]/table/tfoot/tr/td/div/strong")  
    initial_total_price = int(total_price_element.text.replace(",", "").replace("원", ""))

    # 상품 단가 가져오기
    unit_price_element = driver.find_element(By.XPATH, "//*[@id='cartWrap']/div[2]/div[1]/table/tbody/tr/td[6]/div")
    unit_price = int(unit_price_element.text.replace(",", "").replace("원", ""))

    # 수량 추가 테스트
    cart_page.add_count()
    time.sleep(2)

    #수량 확인
    cart_page.count_request()

    # 추가 후 총 금액 검증
    updated_total_price_element = driver.find_element(By.XPATH, "//*[@id='cartWrap']/div[2]/div[1]/table/tfoot/tr/td[6]/strong")
    updated_total_price = int(updated_total_price_element.text.replace(",", "").replace("원", ""))
    assert updated_total_price == initial_total_price + unit_price, "❌ 수량 추가에 따른 총 금액 증가 검증 실패"

    # 수량 감소 테스트
    cart_page.minus_count()
    time.sleep(2)

    #수량 확인
    cart_page.count_request()
    time.sleep(2)

    # 감소 후 총 금액 검증
    final_total_price_element = driver.find_element(By.XPATH, "//*[@id='cartWrap']/div[2]/div[1]/table/tfoot/tr/td[6]/strong")
    final_total_price = int(final_total_price_element.text.replace(",", "").replace("원", ""))
    assert final_total_price == updated_total_price - unit_price, "❌ 수량 감소에 따른 총 금액 감소 검증 실패"

    print("🎉 테스트 성공: 수량 변경에 따른 총 금액 변화가 올바르게 반영됩니다.")

except Exception as e:
    print(f"❗ 오류 발생: {e}")

finally:
    # 웹드라이버 종료
    driver.quit()
