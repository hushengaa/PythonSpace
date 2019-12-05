
import threading

class gettext(threading.Thread):
    def __init__(self,threadName,lock):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.lock = lock
    def run(self):
        #把共有资源锁起来
        self.lock.acquire()
        print(self.threadName)
        #操作完成后打开锁
        self.lock.release()


#保存所有线程的列表
threads = []
threading.Lock()

#创建锁
lock = threading.RLock()

#创建5个线程
for i in range(5):
    #创建一个线程
    thread = gettext('Thread-'+str(i),lock)
    #将创建好的线程添加到线程列表
    threads.append(thread)
    #启动线程
    thread.start()

#等待所有线程结束
for t in threads:
    t.join()

print('线程结束')

