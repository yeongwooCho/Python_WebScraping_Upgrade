from selenium import webdriver
from bs4 import BeautifulSoup
import time


url = "https://daum.net"
options = webdriver.ChromeOptions()
options.headless=True
options.add_argument('window-size=1920x1080')

browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get(url)

browser.find_element_by_xpath('//*[@id="q"]').send_keys('송파 헬리오시티')
browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]').click()

soup = BeautifulSoup(browser.page_source, 'lxml')
pages = soup.find('table', attrs={'class': 'tbl'}).find_all('tr')

# 여기서 파일을 썻을때 해당 데이터가 존재한다면 requests만으로도 충분히 데이터를 긁어올 수 있다.
# 만약 없다면, 동적페이지에 해당하는 것이고, 이때는 selenium을 사용해야 한다.
# with open('quiz.html', 'w', encoding='utf8') as f:
#     f.write(soup.preettify())

cnt = 0
for page in pages[1:]:
    cnt += 1
    print(f'=========== 매물 {cnt} ==========')
    datas = page.find_all('td')
    print('거래 : ', datas[0].get_text().strip())
    print('면적 : ', datas[1].get_text().strip())
    print('가격 : ', datas[2].get_text().strip())
    print('동 : ', datas[3].get_text().strip())
    print('층 : ', datas[4].get_text().strip())
    
browser.quit()