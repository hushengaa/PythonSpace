import time
import requests

#根据游览器的XHR的json文件抓
with open('/Work/test/DoubanMovie1.csv','w',encoding='utf-8') as f:
    #爬取豆瓣科幻电影前100页信息
    for a in range(3):
        url='https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start={}&genres=%E7%A7%91%E5%B9%BB'.format(a*20)
        file=requests.get(url).json() #获取json文件
        time.sleep(2)

        for i in range(20):
            dict=file['data'][i]
            title=dict['title']
            directors=dict['directors']
            rate=dict['rate']
            cast=dict['casts']
            urlname=dict['url']

            #print("{} {} {}\n{}".format(title,rate,' '.join(cast),urlname))
            f.write("{},{},{},{},{}\n".format(title,rate,' '.join(directors),' '.join(cast),urlname))