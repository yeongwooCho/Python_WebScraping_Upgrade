# 네이버 코스피 시가총액 순위

import csv
import requests
from bs4 import BeautifulSoup

# newline='' 이게 없으면 데이터가 이렇게 띄어져서 나온다.
# 1, 삼성전자, 58,200...

# 2, SK하이닉스, 81,300'... 
# text로 열 때는 괜찮지만, excel로 열때 문제가 된다면 encoding='utf-8-sig'
 

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding='utf-8-sig', newline='')
writer = csv.writer(f)

title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실'
title = title.split('\t') # ['N', '종목명', '현재가', ...]
writer.writerow(title)

for page in range(1,5):
    url = f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={page}"
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')

    data_rows = table = soup.find('table', attrs={'class': 'type_2'}).find('tbody').find_all('tr')
    for row in data_rows:
        columns = row.find_all('td')
        if len(columns) <= 1: # 의미없는 데이터 skip
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)