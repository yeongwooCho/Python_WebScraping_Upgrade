import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday.nhn'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

# 네이버 웹툰 전체 목록 가져오기
# class 속성이 title인 모든 "a" element를 반환
cartoons = soup.find_all('a', attrs={'class': 'title'})
print(cartoons)
for cartoon in cartoons:
    print(cartoon.get_text())
