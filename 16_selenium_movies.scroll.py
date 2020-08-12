# Selenium을 통한 동적페이지 스크롤
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

url = 'https://play.google.com/store/movies/top'
browser.get(url)

# 지정한 위치로 스크롤 내리기
# Selenium에서는 JavaScript의 코드를 바로 실행할 수 있다.
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)") # 1920 X 1080의 세로만큼 스크롤을 내려라

# 화면 가장 아래로 스크롤 내리기
# 우리는 맨밑으로 내리고 업데이트되면 다시 맨밑으로 내리고를 반복해야한다.
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') # 현재 문서의 총 높이만큼 스크롤을 내린다.


import time
interval = 3 # 2초에 한번씩 스크롤 내림

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
    if prev_height == curr_height: # 이 두개가 같다는 말은 끝에 도착했다는 뜻이다.
        break

    prev_height = curr_height # 현재는 과거가 되었다.

print('스크롤 완료')



import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, 'lxml')

# 리스트로 묶으면 해당하는 모든 요소들을 다 가져온다. OR 관계로 이해하면 된다
# movies = soup.find_all('div', attrs={'class': ['ImZGtf mpg5gc', 'Vpfmgd'] })
movies = soup.find_all('div', attrs={'class': 'Vpfmgd' })
print(len(movies))  # 0이 나옴

for movie in movies:
    if movie.find('span', {'class': 'SUZt4c djCuy'}):
        title = movie.find('div', attrs={'class': 'WsMG1c nnK0zc'}).get_text()
        link = 'https://play.google.com' + movie.find('a', attrs={'class': "JC71ub"})['href']
        print(title, link)
