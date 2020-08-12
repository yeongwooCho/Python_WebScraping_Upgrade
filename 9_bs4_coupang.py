# http 프로토콜을 이용해서 서버에 요청을 보내면 서버는 요청에 맞은 응답을 보내주는데
# 여기에는 http method라는 것이 존재한다. 그중에서 GET 와 POST 방식에 대해 알아보자
# GET 방식 : 어떤 내용을 누구나 볼 수 있게 url에 적어서 보내는 방식
# https://www.coupang.com/np/search?minPrice=1000&maxPrice=100000&page=1
# ?뒤에 변수와 값 그리고 그것들이 & 로 이어서 존재한다.
# 한번 전송할 때 보낼수 있는 데이터 양의 제한이 존재해서, 큰 데이터는 보내지 못한다.

# POST 방식 : url이 아닌 http 메시지 바디에 숨겨서 보내는 방식이다.
# https://www.coupang.com/np/search?id=nadocoding&pw=1234
# id와 password는 위와같이 하면 너무 노출이 되기에 숨겨서 보낼 수가 있다.
# GET에 비해서는 안전하며, 보낼 수 있는 데이터의 양의 제한이 없기에 파일 업로드와 더불어서 다양한 데이터를 보낼 수가 있다.
# 개인정보를 담은 회원가입이나, 게시판 글쓰기를 할 때는 POST 방식을 사용하게 된다.

import requests
from bs4 import BeautifulSoup
import re

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

# 광고가 있는 것과 없는 것의 차이가 class에서 조금의 차이가 존재하니 정규식을 통해서 이를 구분하여 들고오고록 하자
# 이렇게 되면 class 명이 search-product로 시작하는 모든 li 태그를 갖고 온다.
items = soup.find_all('li', attrs={'class': re.compile('^search-product')})
# print(items[0].find('div', attrs={'class': 'name'}).get_text())

for item in items:
    # 광고제품은 제외
    ad_badge = item.find('span', attrs={'class': 'ad-badge-text'})
    if ad_badge:
        print('<광고제품은 제외합니다.>')
        continue

    name = item.find('div', attrs={'class': 'name'}).get_text()  # 제품명

    # 애플 제품 제외
    if 'Apple' in name:
        print('Apple제품은 제외합니다')
        continue


    price = item.find(
        'strong', attrs={'class': 'price-value'}).get_text()  # 가격정보

    rate = item.find('em', attrs={'class': "rating"})  # 평점 (없는 경우가 존재한다.)
    if rate:
        rate = rate.get_text()
    else:
        rate = '평점 없음'
        print('<평점 없는 상품은 제외합니다.>')
        continue

    rate_cnt = item.find('span', attrs={'class': 'rating-total-count'})  # 평점 수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()[1:-1]
    else:
        rate_cnt = '평점 수 없음'
        print('<평점 수 없는 상품은 제외합니다.>')
        continue

    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)

