# Selenium : 웹페이지 테스트 자동화를 할 수 있는 굉장히 유명한 프레임 워크이다.
# 웹을 띄워서 글자를 입력하고 클릭도 할 수 있는 프레임 워크이다.
# 우리는 네이버 메일 정보는 가져올 수 없다. 그것을 가져오는 작업을 해보자
# pip install selenium

# 웹 드라이버를 설치해야 한다. 브라우져마다 다른 드라이버를 갖는다. 우리는 크롬 드라이버를 사용하자
# 이를 위해서는 내 컴퓨터에 설치되어 있는 크롬의 버전과 호환이 되는 버젼을 설치해야 하기에 크롬버젼을 확인해야한다.
# 크롬 url 창에서 "chrome://version" 을 검색하자 또는 설정의 도움말에서 확인할 수도 있다. #84.0.4147.125
# https://chromedriver.chromium.org/downloads 에서 버전과 OS를 일치하게 설치한다.
# 이 파일을 현재 디렉토리에 압출풀기를 한다. 크롬드라이버.exe가 있으면 이것으로 크롬을 제어할 수 있다.

from selenium import webdriver

browser = webdriver.Chrome()  # 이것처럼 다른폴더에 있을때에는 경로를 지정해주어야함
# browser = webdriver.Chrome() # 크롬 웹드라이버 객체 생성 후 naver.com에 접근
browser.get('http://naver.com')

# >>> elem = browser.find_element_by_class_name("link_login")
# >>> elem
# <selenium.webdriver.remote.webelement.WebElement (session="23bdb659528c80b74712cf831933eefe", element="5afbeadb-e9e5-492f-8dc7-b03d7d5c1770")>
# >>> elem.click() # 클릭하기
# >>> browser.back() # 뒤로가기
# >>> browser.forward() # 앞으로 가기
# >>> browser.refresh() # 새로고침
# >>> elem = browser.find_element_by_id("query")
#
# >>> from selenium.webdriver.common.keys import Keys
# >>> elem.send_keys("나도코딩") # 이건 그냥가능
# >>> elem.send_keys(Keys.ENTER) # Keys.ENTER을 위해 Keys를 import한것

# elem = browser.find_element_by_tag_name("a") # 하나
# elem = browser.find_elements_by_tag_name("a") # 전부

# >>> for e in elem:
# ...     e.get_attribute("href") # href 속성 가져오기


# # Xpath 이용!!!
# >>> elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
# >>> elem
# <selenium.webdriver.remote.webelement.WebElement (session="4ec22a4c857d552dc65daad095c34212", element="619f298b-a908-43f6-b21d-98bc62fabbf3")>
# >>> elem.click()
# 위에서는 그냥 Enter를 누른것이고 xpath는 정확히 그 버튼을 누른 것이다.

# browser.close() # 탭 하나 닫는것
# browser.quit() # 탭이 몇개든 상관없이 전부 닫는 것
