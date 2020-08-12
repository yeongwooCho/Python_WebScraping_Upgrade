import requests

res = requests.get("http://google.com")
print('응답코드', res.status_code) # 200정상

re = requests.get("http://nadocoding.tistory.com")
print('응답코드', re.status_code) # 403 접근권한 없음
# 여기서는 접근권한이 없기에 정상적으로 html 문서를 스크래핑 할 수 없다.(다른방법)

# if re.status_code == requests.codes.ok: # 200인 경우(200으로 해도됨)
#     print("정상입니다.")
# else:
#     print(f"문제가 생겼습니다. 에러코드[{re.status_code}]")

# 정상적으로 html문서를 가져왔다면 문제가 없고, 그렇지 않은 경우에는 에러를 발생시킨다.
res.raise_for_status() # get이랑 쌍을 이룬다.
print("웹 스크래핑을 진행합니다.")


with open('mygoogle.html', 'w', encoding='utf8') as f:
    f.write(res.text)
