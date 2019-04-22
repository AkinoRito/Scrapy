from selenium import webdriver
import time

URL = 'https://www.reddit.com/r/THEMATRIXAI'
RELOAD_TIMES = 50
OUTPUT_RESULT_PATH = 'C:\\Users\\gjy\\Desktop\\WORK\\crawler\\result000.csv'


def main():
    """
    1. initialize a webdriver
    2. load and reload the web page
    3. crawl data
    :return:
    """
    browser = webdriver.Chrome()
    browser.get(URL)
    time.sleep(2)

    # 滚动加载页面
    js = 'window.scrollTo(0, document.body.scrollHeight);'
    for _ in range(RELOAD_TIMES):
        browser.execute_script(js)
        time.sleep(8)

    f_result = open(OUTPUT_RESULT_PATH, 'w', encoding='utf8')
    f_result.write("user,time,content,kind\n")

    # 分享内容爬取 kind = 'shared'
    name_share = browser.find_elements_by_xpath('//*[@class="rpBJOHq2PR60pnwJlUyP0 mos4kc-0 hvBaPD"]'
                                                '/div/div/div/div[2]/article/div[1]/div[1]/div/div/div/a')
    time_share = browser.find_elements_by_xpath('//*[@class="rpBJOHq2PR60pnwJlUyP0 mos4kc-0 hvBaPD"]'
                                                '/div/div/div/div[2]/article/div[1]/div[1]/div/div/a')
    data_share = browser.find_elements_by_xpath('//*[@class="rpBJOHq2PR60pnwJlUyP0 mos4kc-0 hvBaPD"]'
                                                '/div/div/div/div[2]/article/div[1]/div[3]/a')

    print("分享内容个数：", len(name_share))

    for i in range(len(name_share)):
        f_result.write(
            name_share[i].get_attribute('text') + ',' + time_share[i].get_attribute('text') + ',"' +
            data_share[i].get_attribute('href') + '",shared\n')

    # reddit发布的内容爬取 kind = 'article'
    box = browser.find_elements_by_xpath('//*[@class="rpBJOHq2PR60pnwJlUyP0 mos4kc-0 hvBaPD"]/div')
    name_article = []
    time_article = []
    data_article = []
    for i in box:
        name_article.append(i.find_elements_by_xpath('.//div/div/div[2]/div[1]/div/div[1]/div/a'))
        time_article.append(i.find_elements_by_xpath('.//div/div/div[2]/div[1]/div/div[1]/a'))
        data_article.append(i.find_elements_by_xpath('.//div/div/div[2]/div[3]/div/div'))

    for i, j, k in zip(name_article, time_article, data_article):

        # write into result.csv
        if len(k) == 0:  # these are subreddits with only a youtube video
            continue

        if len(i):  # user
            f_result.write(i[0].get_attribute('text')+',')
        else:
            f_result.write('null,')

        if len(j):  # time
            f_result.write(j[0].get_attribute('outerText') + ',"')
        else:
            f_result.write('null,"')

        f_result.write(k[0].get_attribute('outerText') + '",article\n')

    browser.close()
    f_result.close()


if __name__ == '__main__':
    main()
