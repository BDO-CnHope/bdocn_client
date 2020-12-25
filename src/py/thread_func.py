# @Time    : 2020/12/24
# @Author  : Naunter
# @Page    : https://github.com/Naunters

from threading import Thread 

def thread_it(func, *args):
    t = Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()
    #t.join()