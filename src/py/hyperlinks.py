# @Time    : 2021/03/18
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from webbrowser import open_new
from time_template import time_template

def hyperlinks(var):
    time_template()
    print("hyperlinks.py >>> def hyperlinks(var): ")
    if var == 1 :
        print("hyperlinks.py >>> def hyperlinks(var): var: " + str(var))
        open_new(r"https://github.com/BDO-CnHope/bdocn_client")
    elif var == 2:
        print("hyperlinks.py >>> def hyperlinks(var): var: " + str(var))
        open_new(r"https://www.bilibili.com/video/BV1yf4y1s75B")