# 동적페이지란 페이지가 접속될 때 바로 불러와지는 것이 아닌 사용자가 어떤 동작을 했을 때 동작하는 웹페이지이다.
# 예를 들어, 스크롤을 내렸을 떄, 새로운 목록을 갱신한다던지 그런 작업이다.
# google 영화 정보를 받아오자
# 인기차트 중에서 할인하고 있는 영화정보만 빼오는 작업을 수행하자
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://play.google.com/store/movies/top'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'Accept-Language': 'ko-KR,ko'  # 한글 페이지가 있으면 주고, 없으면 기본페이지를 준다.
}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

movies = soup.find_all('div', attrs={'class': 'ImZGtf mpg5gc'})
print(len(movies))  # 0이 나옴

# 왜 0이 나왔는지 살펴보기 위해서 파일에 써보자
with open('movie.html', 'w', encoding='utf-8-sig') as f:
    # f.write(res.text) # 너무 보기 힘듬
    f.write(soup.prettify())  # html문서를 이쁘게 보여줌
# 영어에다가 순위랑 구조도 조금씩 다르게 html문서로 보여지게 됨(열어봐)
# 해당 브라우저는 사용자의 headers 의 user agent 정보에 따라 다른 형태의 웹페이지를 보여줌
# 크롬으로 들어갔을 때는 대한민국에서 크롬으로 들어갔을 때의 내용이 있는 것이다. -> User Agent 정보전달 ㄱㄱ
# 언어 바꾸기는 encoding='utf-8-sig'로 수정하거나 headers에서 한글 웹페이지를 달라고 요청할 수 있다.
# Accept-Language 없이 해도 html로 열면 글자는 깨져도 한국페이지로 나옴, encoding='utf-8-sig' 수정하면 글자 까지도 나옴(내방법)
# 이렇게 하지 않더라도 html에서 text는 정상적인 한글로 되어있기에 스크래핑은 문제없긴한 (나도코딩 방법)


# 근데 왜 10밖에 안나오는가? 자세히 보면 10개가 먼저뜨고, 나머지가 뜬다. 그리고 스트롤을 내리면 새로운 영화정보가 업데이트 된다.
# requests로 가져올 수 있는 것은 10개 뿐이다. 나머지는 반응형 동적웹페이지의 반응 데이터이기에 가져올 수 없다.
# 그때, 사용하는 것이 Selenium 이다.
