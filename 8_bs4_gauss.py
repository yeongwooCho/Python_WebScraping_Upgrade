import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

cartoons = soup.find_all("td", attrs={'class': 'title'})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"] # 앞에 https://comic.naver.com 이 존재한다.
# print(title)
# print("https://comic.naver.com" + link)

# # 만화제목, 링크와 평점
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a['href']
#     star = cartoon.find_next_sibling('td').strong.get_text()
#     print(title, link, star)

# 평균평점구하기
total_rates = 0
cartoons = soup.find_all('div', attrs={'class': 'rating_type'})
for cartoon in cartoons:
    rate = cartoon.find('strong').get_text()
    total_rates += float(rate)
total_rates /= len(cartoons)
print(total_rates)

# 프로그래밍 언어에는 interpreter 언어와 compile언어가 존재한다.
# 컴파일 방식의 경우 기계어로 바뀌는 작업이 이루어 진다음 실행이 된다.
# 파이썬의 경우는 interpreter언어이고 한줄씩 바로바로 실행이 가능하다
# 터미널에서 python을 치면 된다. exit() 로 탈출가능
# beautifulsoup의 경우 한국어와 영어로 설명서가 존재한다.
