# -*- coding: utf-8 -*-
# @Time    : 2020/12/24
# @Author  : Naunter
# @Page    : https://github.com/Naunters

import threading

def thread_it(func, args):
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()
    #t.join()