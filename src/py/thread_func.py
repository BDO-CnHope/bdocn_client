# @Time    : 2021/03/14
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from threading import Thread
from datetime import datetime

time_stamp = datetime.now()

# 多线程任务
def thread_it(func, *args):
    print("[BEGIN] thread_it >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
    t = Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()
    #t.join()