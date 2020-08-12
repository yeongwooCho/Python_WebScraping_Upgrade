# 웹사이트에 접근할때 웹사이트에서는 header정보를 통해 알 수 있다.
# pc, 스마트폰으로 접근하는 가에 따라 다른 브라우져가 나오는 것이 그에 대한 반응을 설정을 해놓은 것이다.
# 웹 스크래퍼가 접근한다면 그것을 확인해서 접속을 확인해서 차단하는 경우가 존재한다.
# 이럴때 우리가 사용하는 것이 User agent 이다.
# https://www.whatismybrowser.com/detect/what-is-my-user-agent 에 위에 존재하는 것이 useragent의 정보이다.
# 접속하는 웹 브라우져에 따라서 user agent가 다르다
import requests

url = "http://nadocoding.tistory.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
# 나의 user agent 값을 hearers의 정보로 전달하여 내가 크롬으로 접근함을 알린다.!!!!(핵심!!!)
res = requests.get(url, headers=headers)
res.raise_for_status()

with open('nadocoding.html', 'w', encoding='utf8') as f:
    f.write(res.text)
