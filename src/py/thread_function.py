# @Time    : 2021/03/15
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from threading import Thread
from time_template import time_template

def thread_it(func, *args):
    time_template()
    print("thread_function.py >>> def thread_it(func, *args)")

    t = Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()