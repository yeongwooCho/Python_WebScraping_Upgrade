# 네이버 웹툰의 정보를 빼오자
# pip install beautifulsoup4 : 실제로 우리가 스크래핑하기 위한 패키지
# pip install lxml : 구문을 분석하는 parser

import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday.nhn'
res = requests.get(url)
res.raise_for_status()

# 우리가 가져온 html문서를 lxml파서를 통해서 BeautifulSoup 객체로 만든다. soup는 모든 정보를 다 갖고있다.
soup = BeautifulSoup(res.text, "lxml")
print(soup.title, type(soup.title))  # title 태그를 가져온다
print(soup.title.get_text(), type(soup.title.get_text()))  # title 태그의 text를 가져온다
print(soup.a)  # soup 객체에서 처음 발견되는 a element 출력
print(soup.a.attrs)  # a element 의 속성 정보를 출력
print(soup.a['href'])  # a element 의 href 속성 '값' 정보를 출력

print(soup.find('a', attrs={'class': 'Nbtn_upload'}))  # 해당하는 것 중에서 처음 발견되는 것
print(soup.find(attrs={'class': 'Nbtn_upload'}))  # 웹툰올리기가 하나 뿐이니깐 다음과 같이 사용 가능
print(soup.find('a', {'class': 'Nbtn_upload'}))


# 형제, 부모, 자식으로 가는 것
rank1 = soup.find('li', attrs={'class': 'rank01'})
print(rank1.a)
print(rank1.a.get_text())
# next_sibling는 다음 요소로, previous_sibling는 이전 요소로 간다.
print(rank1.next_sibling)  # next element로 넘어감
# 한번하면 아무것도 안나오고 두번하니깐 나오네(줄바꿈때문에 이런경우가 생기기도함)
print(rank1.next_sibling.next_sibling)
# 부모로 가는 것
print(rank1.parent)

# next_sibling가 두번 이루어 지는 것이 있고, 아닌 것이 있으면 구분하기 귀찮을 때 사용하는 방법
rank2 = rank1.find_next_sibling('li')  # 다음 li 태그를 찾는 것이다.!!!!!!!!!!!!!!!!
print(rank2.a.get_text())

# 한번에 다 찾은 다음 분석할 때
ranks = rank1.find_next_siblings('li')  # 형재들을 가져온다.
print(ranks)
for rank in ranks:
    print(rank.a.get_text().strip())


# text를 통해서도 find를 할수가 있다.
webtoon = soup.find('a', text="외모지상주의")
print(webtoon)
