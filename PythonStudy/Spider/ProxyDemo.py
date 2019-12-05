'''
from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxy='54.37.131.161:3128'
proxy_handler=ProxyHandler({
    'http':'http://'+proxy,
    'https':'https://'+proxy
})
opener=build_opener(proxy_handler)
try:
    response=opener.open('https://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

     {"https" : "54.37.131.161:3128"},
    {"https" : "54.37.131.84:3128"},
    {"https" : "78.41.53.39:8080"},
    {"https" : "184.185.161.65:3128"},
    {"https" : "178.128.42.138:8888"},
'''

import urllib.request
import random

proxy_list = [
    #可用代理IP
    {"https" : "183.177.98.6:8080"},
]

# 随机选择一个代理
proxy = random.choice(proxy_list)
# 使用选择的代理构建代理处理器对象
httpproxy_handler = urllib.request.ProxyHandler(proxy)

opener = urllib.request.build_opener(httpproxy_handler)

request = urllib.request.Request("https://httpbin.org/get")
response = opener.open(request)
print (response.read().decode())


