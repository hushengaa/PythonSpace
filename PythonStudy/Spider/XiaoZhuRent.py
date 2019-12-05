import time
from lxml import etree
import requests

with open('/Work/test/xzzf.csv','w',encoding='utf-8') as f:
    #爬取小猪短租前1页的租房信息
    for a in range(1,11):
        url='https://cs.xiaozhu.com/yuelu-duanzufang-p{}-8/?housetyperoomcnt=yiju%7C'.format(a)
        data=requests.get(url).text

        s=etree.HTML(data)
        file=s.xpath('//*[@id="page_list"]/ul/li')
        time.sleep(3)

        for div in file:
            title=div.xpath('./div[2]/div/a/span/text()')[0]
            price=div.xpath('./div[2]/div[1]/span[1]/i/text()')[0]
            scribe=div.xpath('./div[2]/div/em/text()')[0].strip()
            pic=div.xpath('./a/img/@lazy_src')[0]

            #print("{} {} {}\n{}".format(title,price,scribe,pic))
            f.write("{},{},{},{}\n".format(title,price,scribe,pic))




