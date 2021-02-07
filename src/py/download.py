# @Time    : 2020/12/25
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

# reference
# cd "C:\Users\user-edu\AppData\Local\Programs\Python\Python39\Scripts"
# python3 -m pip install requests
# https://www.w3schools.com/python/module_requests.asp
# https://www.tutorialspoint.com/downloading-files-from-web-using-python
# https://www.programmersought.com/article/3277959585/
# https://toodo.fun/funs/learn/files/article_frame.php?id=72
# Python实现多进程/多线程同时下载单个文件
# https://blog.csdn.net/dongfuguo/article/details/104995567
# https://www.fatalerrors.org/a/single-file-source-under-python-multithreading.html
# https://zhuanlan.zhihu.com/p/162965342

from urllib.request import build_opener,install_opener,urlretrieve,urlopen,Request
from re import findall
from ran_useragent import GetUserAgent
import ui4

def download_file(url, todir, tofilename):
    path = todir + '\\' + tofilename
    user_agent = GetUserAgent()
    opener = build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    install_opener(opener)
    urlretrieve(url, path)
    print('download '+url+' to '+path)
    

def download_split_files(url, todir):
    user_agent = GetUserAgent()
    header = {"User-Agent":user_agent,}
    add_header = Request(url, headers=header)
    dl_link = urlopen(add_header)
    data = dl_link.read().decode('utf-8')
    filter_data = findall(r'>part[0-9][0-9][0-9][0-9]</a>',data)
    hrefs = []
    hrefs.clear()

    if 'github' in url and 'split_font' in url:
        raw_url = 'https://github.com/BDO-CnHope/bdocn/raw/master/split_font/'
    elif 'github' in url and 'split_font' not in url:
        raw_url = 'https://github.com/BDO-CnHope/bdocn/raw/master/split/'
    elif 'gitee' in url and 'split_font' in url:
        raw_url = 'https://gitee.com/bdo-cnhope/bdocn/raw/master/split_font/'
    elif 'gitee' in url and 'split_font' not in url:
        raw_url = 'https://gitee.com/bdo-cnhope/bdocn/raw/master/split/'
    else:
        pass

    for i in filter_data:
        href = findall(r'>(.*)</a>',i)
        href = str(href)
        href = href.replace(">",'')
        href = href.replace("</a>",'')
        href = href.replace("['",'')
        href = href.replace("']",'')
        hrefs.append(href)
    
    for filename in hrefs:
        full_url = ''
        full_url = raw_url + '/' + filename
        download_file(full_url, todir, filename)

def download_en_loc():
    en_loc_ver = 'http://akamai-gamecdn.blackdesertonline.com/live001/game/config/config.language.version'
    user_agent = GetUserAgent()
    opener = build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    install_opener(opener)
    a = urlopen(en_loc_ver)
    version = a.read().decode('utf-8')
    en_loc_zip = 'http://akamai-gamecdn.blackdesertonline.com/live001/game/language/BDOLanguage_' + version + '.zip'
    return(en_loc_zip)