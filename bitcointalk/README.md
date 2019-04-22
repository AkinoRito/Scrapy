# Bitcointalk爬虫程序

### 执行程序命令

```shell
$ cd bitcointalk
$ scrapy runspider bitcoin
```



### Requirements

1. scrapy
2. bs4
3. re



### 爬取内容

1. user name

2. user status

3. activity

4. merit

5. title of the article

6. time to post the article

7. context of the article

   

### 遇到的坑

1. scrapy不识别 `tbody` 标签。尽管浏览器在解析时会显示 `tbody` 标签，但是在xpath中只要把 `tbody` 全部忽略，就能得到正确的结果。

2. 在爬取时间时会出现爬取不完整的情况，如每个网页显示20条article，但是实际上只能爬到十几条时间信息。检查不同的时间所在xpath，可见典型的两种xpath为：

   > //*[@id="quickModForm"]/table[1]/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/div[2]/span[1]

   和

   > //*[@id="quickModForm"]/table[1]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/div[2]

   差别就在于最里一层是否有 `span` 标签。

   解决方法：爬取到最后的 `div[2]` 标签中的内容，这一步得到的结果是包含时间的字符串或者一段包含时间的html代码。由于日期的格式统一，都是 “月份 日期，年份，详细时间” 格式，接下来使用正则表达式匹配到日期信息即可。

3. 有的class是动态生成的，每次刷新得到的class都不同。解决方法：xpath的构造中避开用class查找，尽量用一层层的标签查找。

4. class="smalltext"里爬取不到文本信息，爬到的都是\n\t。

   解决方法：先找到 `smalltext` 中的全部内容，extract()出来，再进一步用正则表达式等方法匹配得到具体内容。