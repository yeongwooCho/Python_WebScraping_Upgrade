# 영화정보 가져오기
# 여기서 이미지를 저장하려면 클릭 3번이 이루어 져야 한다.

import requests
from bs4 import BeautifulSoup

for year in range(2015, 2020):

    url = f'https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    images = soup.find_all('img', attrs={'class': 'thumb_img'})

    for idx, image in enumerate(images):
        image_url = image['src']
        if image_url.startswith('//'):
            image_url = 'https:' + image_url

        print(image_url)

        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open(f'movie{year}_{idx + 1}.jpg', 'wb') as f:  # 이미지는 text data가 아니다
            f.write(image_res.content)  # content정보를 바로 쓰는 것이다.

        if idx >= 4:
            break
