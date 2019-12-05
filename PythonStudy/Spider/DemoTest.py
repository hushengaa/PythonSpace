"""
novel = [(['a']*2) for i in range(3)]

tea = [['a' for y in range(2)] for t in range(3)]
print(tea)
print(novel)

import tesserocr
from PIL import Image
import pymysql
import pymongo
import redis

print(redis.VERSION)
print(pymongo.version)
print(pymysql.VERSION)
image = Image.open('/Users/husheng/Desktop/ocrpic.png')
print(tesserocr.image_to_text(image))
print(tesserocr.file_to_text('/Users/husheng/Desktop/ocrpic.png'))

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RedirectHandler):
    def get(self):
        self.write("Hello,world!")

def make_app():
    return tornado.web.Application([
        (r"/",MainHandler),
    ])

if __name__ =="__main__":
    app=make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


from scrapyd_api import ScrapydAPI

scrapyd = ScrapydAPI('http: // localhost:6800')
print(scrapyd.list_projects())

import turtle
from turtle import *
def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.setup(600, 600)
    turtle.pen(speed=10, pencolor='blue')
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(1)
    level = 5
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle()
    done()
main()
"""

'''
# -*- coding: utf-8 -*-
import cv2
import logging

# 设置日志
logging.basicConfig(level = logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# 待检测的图片路径
ImagePath = '/Work/test/wuyanzu.jpg'

# 读取图片
logger.info('Reading image...')
image = cv2.imread(ImagePath)
# 把图片转换为灰度模式
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 探测图片中的人脸
logger.info('Detect faces...')
# 获取训练好的人脸的参数数据,进行人脸检测
face_cascade = cv2.CascadeClassifier('/Work/test/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(3, 3))

search_info = "Find %d face."%len(faces) if len(faces) <= 1 else "Find %d faces."%len(faces)
logger.info(search_info)

# 绘制人脸的矩形区域(红色边框)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)

# 显示图片
cv2.imshow('Find faces!', image)
cv2.waitKey(0)

'''
# -*- coding: utf-8 -*-
import cv2
import logging

# 设置日志
logging.basicConfig(level = logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# 待检测的图片路径
ImagePath = '/Work/test/cat.jpg'

# 读取图片
logger.info('Reading image...')
image = cv2.imread(ImagePath)
# 把图片转换为灰度模式
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 探测图片中的人脸
logger.info('Detect faces...')
# 获取训练好的人脸的参数数据,进行人脸检测
face_cascade = cv2.CascadeClassifier('/Work/test/opencv-master/data/haarcascades/haarcascade_frontalcatface.xml')
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(3, 3))

search_info = "Find %d face."%len(faces) if len(faces) <= 1 else "Find %d faces."%len(faces)
logger.info(search_info)

# 绘制人脸的矩形区域(红色边框)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)

# 显示图片
cv2.imshow('Find faces!', image)
cv2.waitKey(0)
