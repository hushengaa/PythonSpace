import requests
import os
from bs4 import BeautifulSoup

url = 'https://www.50zww.com/book_22/23116.html'
re_header = {
    'Referer':'https://www.50zww.com/book_22/23116.html',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

#获取网页
r = requests.get(url,params=re_header)

#更改编码
r.encoding = 'gbk'

#获得BeautifulSoup对象
soup = BeautifulSoup(r.text,"html.parser")

#获得章节内容
chapter_content = soup.select('#htmlContent')[0].text

#打开/创建文件
fo = open('/Work/test/1.txt','wb')

fo.write((chapter_content).encode('utf-8'))

print(chapter_content)

#使用完后关闭文件
fo.close()

print('下载成功')
