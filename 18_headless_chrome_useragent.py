from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")


browser = webdriver.Chrome(options=options)
browser.maximize_window()

# user-agent-string 를 가져오자
url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
browser.get(url)

user_agent = browser.find_element_by_id('detected_value').text
print(user_agent)
# 실제 : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36
# 코드 : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/84.0.4147.125 Safari/537.36
# 문제는 HeadlessChrome 로 표시가 된다. 이렇게 되면 막히는 사이트가 생길 수 있으니 이를 방지하자
# 위에 options.add_argument("user-agent='실제 크롬에서의 나의 유저 에이전트값을 전달하면 된다.')
# Headless를 사용할 때에는 필요에 따라 user-agent 값을 바꿔줘야 하는 경우도 발생할 수 있다는 점을 주의하자
browser.quit()

# selenium에 대해 더 필요한 자료는 selenium by python으로 검색하여 공부하자
# https://selenium-python.readthedocs.io/
