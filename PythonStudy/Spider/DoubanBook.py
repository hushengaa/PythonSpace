import time
from lxml import etree
import requests

#根据页面样式里的xpath抓取
with open('/Work/test/bookTop250.docx','w',encoding='utf-8') as f:
    #爬取豆瓣前250位的图书榜
    for a in range(10):
        url='https://book.douban.com/top250?start={}'.format(a*25)
        data=requests.get(url).text

        s=etree.HTML(data)
        file=s.xpath('//*[@id="content"]/div/div[1]/div/table')
        time.sleep(3)

        for div in file:
            title=div.xpath('./tr/td[2]/div[1]/a/@title')[0]
            href=div.xpath('./tr/td[2]/div[1]/a/@href')[0]
            score=div.xpath('./tr/td[2]/div[2]/span[2]/text()')[0]
            num=div.xpath('./tr/td[2]/div[2]/span[3]/text()')[0].strip('(').strip().strip(')')
            scribe=div.xpath('./tr/td[2]/p[2]/span/text()')

            if len(scribe)>0:
                #print("{} {} {} {} {}".format(title,href,score,num,scribe[0]))
                f.write("{},{},{},{},{}\n".format(title,href,score,num,scribe[0]))
            else:
                #print("{} {} {} {}".format(title,href,score,num))
                f.write("{},{},{},{}\n".format(title,href,score,num))


