# 네이버 항공권 비행기 조회
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()  # 화면을 키면 전체화면으로 바꿔서 키워줌

url = 'https://flight.naver.com/flights/'
browser.get(url)  # url로 이동

# browser.find_element_by_class_name('txt_trip').click() 이번에는 가는날 선택이라는 글자로 찾아보자
browser.find_element_by_link_text("가는날 선택").click()

# 출발달의 일과 도착달의 일이 일 관점에서 보면 겹치기에 29를 들고올때는 전부 들고와서 인덱스로 나누자
# 이번달 27, 28일 선택
# browser.find_elements_by_link_text('27')[0].click() # [0] -> 이번달 , # [1] -> 다음달
# browser.find_elements_by_link_text('28')[0].click()
browser.find_elements_by_link_text('27')[0].click()
browser.find_elements_by_link_text('28')[1].click()

# 제주도 선택
# browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]/div/a').click() # 이게 클릭이 안됨 더위로!!!
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()

# 항공권 검색 클릭
browser.find_element_by_link_text('항공권 검색').click()


# 첫번째 결과 출력 (로딩 시간에 의한 에러 발생)
# elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
# 로딩시간을 time.sleep(5) 이렇게 무턱대고 기다리는 작업도 수행 가능하지만,
# 로딩이 끝날때 까지만 기다리도록 하는 기능도 제공한다.!!!!!!!!!!!!!!!!!!!!!!
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait    # 기다려 주는 거네
# from selenium.webdriver.support import expected_conditions as EC
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    print(elem.text)
finally:
    browser.quit()
# 브라우져를 최대 10초동안은 기다리는데,
# 언제까지? expected_conditions 어떤 조건을 기다리는데 위치된 요소의 존재가 조건이야
# 그 조건인 위치된 요소는 XPATH 이며 그 값은 다음과 같음을 묶어서 tuple로 전달해줌
# 보충설명 : XPATH 외에도 ID, CLASS_NAME, LINK_TEXT 등도 사용가능함
