# Headless 크롬
# 이전 강의에서 봤듯이 매번 브라우져를 띄어서 보여지는게 메모리를 많이 잡아먹고 느리다.
# 만약 화면을 볼 필요도 없고, 서버에서 웹 스크래핑 작업을 한다면 브라우져를 띄울 필요가 없다.
# 이때, Headless 기능을 사용하고, 크롬에서는 크롬이 없는 크롬이라하여 Headless 크롬 라고 한다.
# 크롬을 띄우고 않고, 크롬을 쓸 수 있는, 백그라운드에서 동작하도록 하여 보다 빠른 성능으로 매번 똑같은 작업을 할 수 있다.

from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver

# 이렇게만 설정하면 끝이다.
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")  # 해상도에 맞게 브라우져를 내부적으로 띄워서 실행
browser = webdriver.Chrome(options=options)
# headless의 경우 페이지가 어떻게 도는지 확인하기 위한 스크린샷을 제공한다.
# 스크롤완료 뒤에 스크린샷을 찍겠다 -> browser.get_screenshot_as_file("google_movie.png")


browser.maximize_window()

url = 'https://play.google.com/store/movies/top'
browser.get(url)

interval = 3  # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")
# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:  # 이 두개가 같다는 말은 끝에 도착했다는 뜻이다.
        break

    prev_height = curr_height  # 현재는 과거가 되었다.

print('스크롤 완료')

browser.get_screenshot_as_file("google_movie.png")


soup = BeautifulSoup(browser.page_source, 'lxml')

# 리스트로 묶으면 해당하는 모든 요소들을 다 가져온다. OR 관계로 이해하면 된다
# movies = soup.find_all('div', attrs={'class': ['ImZGtf mpg5gc', 'Vpfmgd'] })
movies = soup.find_all('div', attrs={'class': 'Vpfmgd'})
print(len(movies))  # 0이 나옴

for movie in movies:
    if movie.find('span', {'class': 'SUZt4c djCuy'}):
        title = movie.find('div', attrs={'class': 'WsMG1c nnK0zc'}).get_text()
        link = 'https://play.google.com' + \
            movie.find('a', attrs={'class': "JC71ub"})['href']
        print(title, link)

browser.quit()
