# Project : 웹 스크래핑을 이용하여 나만의 비서를 만든다
# 1. 네이버에서 오늘 서울의 날씨 정보를 가져온다
# 2. 헤드라인 뉴스 3건을 가져온다

import requests
from bs4 import BeautifulSoup


# [네이버 오늘의 날씨]

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%B6%80%EC%82%B0%EB%82%A0%EC%94%A8'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')
table = soup.find('div', attrs={'class': 'info_data'})

state = table.find('li').get_text().strip()
cur = table.p.span.get_text().strip()
max_min = soup.find('li', attrs={'class', "date_info today"}).find(
    'dd').find_all('span')
rains = soup.find('li', attrs={'class', "date_info today"}).find_all(
    'span', attrs={'class': 'num'})

print(state)
print(f"{cur}℃\t( 최저 {max_min[0].get_text()}℃ / 최고 {max_min[2].get_text()}℃ )")
print(f'오전 강수확률 {rains[0].get_text()}% / 오후 강수확률 {rains[1].get_text()}%')

print('\n\n')
# =================================================================================================================
# =================================================================================================================

# [헤드라인 뉴스]
url = 'https://news.naver.com/'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

artis = soup.find_all('div', attrs={'class': 'hdline_article_tit'})
for ind, arti in enumerate(artis):
    print(f"{ind}. {arti.get_text().strip()}")
    print(f"(링크 : {arti.a['href']})")

