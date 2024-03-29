# @Time    : 2022/01/01
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from webbrowser import open_new
from urllib.request import urlopen,Request
from time_template import time_template

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'

def test_link(url):
    try:
        print("hyperlinks.py >>> def test_link(url): ")
        header = {"User-Agent":user_agent}
        add_header = Request(url, headers=header)
        resp = urlopen(add_header, timeout=6)
        code = resp.getcode()
        print('hyperlinks.py >>> def test_link(url): code:', code)
        return code
    except:
        print("hyperlinks.py >>> def test_link(url): error")
        return 0

def hyperlinks(var):
    time_template()
    print("hyperlinks.py >>> def hyperlinks(var): ")
    if var == 1 :
        print("hyperlinks.py >>> def hyperlinks(var): var: " + str(var))
        url1=r"https://gitee.com/bdo-cnhope/bdocn_client"
        url2=r"https://github.com/BDO-CnHope/bdocn_client"
        try:
            if test_link(url2) != 200:
                open_new(url1)
            else:
                open_new(url2)
        except:
            open_new(url1)
    elif var == 2:
        print("hyperlinks.py >>> def hyperlinks(var): var: " + str(var))
        url1=r"https://space.bilibili.com/264222/video"
        url2=r"https://cnhope.onehoi.com/bdocn"
        try:
            if test_link(url2) != 200:
                open_new(url1)
            else:
                open_new(url2)
        except:
            open_new(url1)
    elif var == 3:
        print("hyperlinks.py >>> def hyperlinks(var): var: " + str(var))
        #url1=r"https://share.weiyun.com/BtJgJGUX"
        #url2=r"https://github.com/BDO-CnHope/bdocn_client/releases"
        url1=r"https://gitee.com/bdo-cnhope/bdocn_client/blob/main/NEWS.md"
        url2=r"https://github.com/BDO-CnHope/bdocn_client/blob/main/NEWS.md"
        try:
            if test_link(url2) != 200:
                open_new(url1)
            else:
                open_new(url2)
        except:
            open_new(url1)