from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests

THEMSTRIXAI_url = 'https://www.reddit.com/r/THEMATRIXAI/'


def execute_times(driver, times=10):
    """
    实现滚轮滑到页面最下方的功能，每5秒下移一次
    调用示例：execute_times(webdriver.Chrome(), 10)
    :param driver: webdriver
    :param times: 滚轮下移次数
    :return: None
    """
    for i in range(times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)


def main():
    driver = webdriver.Chrome()  # 打开浏览器
    driver.get(THEMSTRIXAI_url)  # 打开网页
    execute_times(driver, 10)
    soup = BeautifulSoup(driver.page_source, 'html5lib')  # page_source 获取当前源码
    # print(soup.prettify())
    # print(soup.contents)
    # print(soup.find(name='').getText('\n'))
    print(soup.get_text())

if __name__ == '__main__':
    main()
