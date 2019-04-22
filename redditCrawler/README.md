# reddit的爬虫程序 reddit.py

### 功能

爬取 `URL` 中的 `user`, `time`, `content`, `kind` 字段。

### REQUIREMENTS

1. 安装Chrome与版本匹配的webdriver。

2. python library: selenium.

### 输入参数

在 `URL` 中指定待爬取URL，在 `RELOAD_TIMES` 中指定动态网页自动下滑加载的次数，在 `OUTPUT_RESULT_PATH` 中指定输出文件的路径。

### 输出

爬取内容以csv格式输出到 `OUTPUT_RESULT_PATH` 指定的文件中。在程序中，保存爬取内容的变量分别为：`name_article` 为保存了发帖人ID的列表，`time_article` 为保存发帖时间的列表，`data_article` 为保存文章内容的列表。