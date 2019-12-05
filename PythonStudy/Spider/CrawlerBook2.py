import time

import requests
from bs4 import BeautifulSoup
import threading

#多线程爬取小说，并以TXT保存在本地

url = 'https://www.50zww.com/book_22/'
re_header = {
    'Referer':'https://www.50zww.com/book_22/',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

chapter_list = []

#获取网页
#更改编码
#获得BeautifulSoup对象
#获取章节列表
r = requests.get(url,params=re_header)
r.encoding = 'gbk'
soup = BeautifulSoup(r.text,"html.parser")
temp_list = soup.select('.chapterlist a')
for t in range(len(temp_list)):
    temp_list[t] = temp_list[t]['href']
chapter_list.extend(temp_list)

for i in range(len(chapter_list)):
    chapter_list[i]=url+chapter_list[i]
    #对每个章节编号
    chapter_list[i] = [i,chapter_list[i]]
    print(chapter_list[i])

class gettext(threading.Thread):
    def __init__(self,chapter_list,book,lock,folock,re_header):
        threading.Thread.__init__(self)
        self.chapter_list = chapter_list
        self.book = book
        self.lock = lock
        self.folock = folock
        self.re_header = re_header
        self.exitflag = False

    def run(self):
        while not self.exitflag:
            #把共有资源锁起来
            self.lock.acquire()
            if len(self.chapter_list) != 0:
                data = self.chapter_list.pop()
                #获得链接后打开锁
                self.lock.release()

                #获取第一页页面
                while 1:
                    r = requests.get(data[1],params=re_header)
                    #成功获得页面跳出循环，否则继续
                    if r.status_code == 200:
                        break
                r.encoding = 'gbk'
                soup = BeautifulSoup(r.text,"html.parser")

                #这个网站把每个章节分为两页，要分两次获取
                #获取章节名和第一页的内容
                title = soup.select('.h1title')[0].text
                content_1 = soup.select('#htmlContent')[0].text

                time.sleep(0.1)

                self.folock.acquire()
                #将章节内容放进储存对象中
                self.book.put(data[0],title,content_1)
                print(title)
                self.folock.release()

            else:
                #chapter_list长度为0时退出线程
                self.exitflag = True
                self.lock.release()
#定义一个storage类用来暂时储存小说内容
class storage:
    def __init__(self):
        self.content = []

    def put(self,index,title,content):
        self.content.extend([[index,title,content]])

#反向列表
chapter_list.reverse()

'''*************************************线程*******************************'''
#保存小说内容的对象
book = storage()
#保存所有线程的列表
threads = []

#创建锁
lock = threading.RLock()
folock = threading.RLock()

#创建10个线程
for i in range(10):
    #创建一个线程
    thread = gettext(chapter_list,book,lock,folock,re_header)
    #将创建好的线程添加到线程列表
    threads.append(thread)
    #启动线程
    thread.start()

#等待所有线程结束
for t in threads:
    t.join()

print('线程结束')

#定义一个二维数组
#novel = [['a','a']]*len(book.content)  这样定义二维数组会出现，因为指针的缘故，改变其中一个值，其余所有值都会被修改！
novel = [(['a']*2) for i in range(len(book.content))]
#另外一种定义二维数组的方法(让指针不是同时指向一个)：novel = [['a' for i in range(2)] for j in range(len(book.content))]

for t in book.content:
    index = t[0]

    print(t)
    #因为python中列表是按引用传递的，所以这里我们传递的只是地址
    novel[index][0] = t

#打开/创建文件
fo = open('/Work/test/完美世界.txt','wb')

for t in novel:
    title = t[0][1]
    chapter_content = t[0][2]

    #写入章节名和内容
    fo.write((title).encode('utf-8'))
    fo.write((chapter_content).encode('utf-8'))

    #打印提示
    print(title + '已下载')


#关闭文件
fo.close()

print('下载成功')
